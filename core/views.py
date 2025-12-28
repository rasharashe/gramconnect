from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from django.shortcuts import render
from core.models import Home, Squad
from accounts.models import User
from .forms import AdminUserCreateForm
from .utils import create_squads, GetSidebarContext
from django.http import HttpResponse, HttpResponseRedirect
import csv
import io

# Create your views here.


class Login(LoginView):
    template_name = 'sign-in.html'


class HomeList(LoginRequiredMixin, ListView):
    model = Home
    context_object_name = 'homes'
    template_name = '_home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['homes'].count()
        context['sidebar'] = GetSidebarContext.get_context(self.request)
        return context
    

class SquadList(LoginRequiredMixin, ListView):
    model = Home
    context_object_name = 'homes'
    template_name = '_home.html'

    def get_queryset(self):
        sqid = self.kwargs.get('sqid')
        squad = Squad.objects.get(sqid=sqid)
        if squad:
            return Home.objects.filter(squad=squad)
        return Home.objects.none()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['homes'].count()
        context['sidebar'] = GetSidebarContext.get_context(self.request)
        return context
    

def bulk_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        upload_file = request.FILES['file']
        # Process the uploaded file here
        # For example, you can read its content or save it to a model
        # ...csv file
        
        # Use TextIOWrapper to read the uploaded byte stream as text
        data_set = upload_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string) # Skip the header row if your CSV has one

        items_to_create = []
        try:
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                if column[0].startswith('AP') or column[0].startswith('BP') or column[8] != 'udf':
                    continue  # Skip header or invalid rows
                # column 0 is like a1, a2, a3 where a is booth 1 or b is booth 2 and 1,2,3 is the serial number in voter list
                booth, no = column[0].strip().lower()[0], column[0].strip().lower()[1:]
                booth = 1 if booth == 'a' else 2
                name, guardians_name = column[1], column[2]
                # need to seperate house number, value is like 2/234 , 2/345 etc i need only 234, 345
                house_number = column[3].split('/')[-1].strip()
                house_name = column[4].strip()
                gender = column[5].split('/')[0].strip().upper()
                sec_id = column[6].strip()
                squad_short_name = column[7].strip().lower()
                if not squad_short_name:
                    squad_short_name = 'rac'
                squad = Squad.objects.get(short_name=squad_short_name)
                home = Home.objects.filter(number=house_number).first()
                if not home:
                    home = Home.objects.create(
                        name=house_name,
                        number=house_number,
                        squad=squad,
                        created_by=request.user,
                        updated_by=request.user,
                    )
                member = home.members.filter(sec_id=sec_id).first()
                if not home.owner:
                    home.owner = member.full_name if member else name
                    home.save()
                if not member:
                    member = home.members.create(
                        full_name=name,
                        guardian_name=guardians_name,
                        gender=gender,
                        sec_id=sec_id,
                        booth=booth,
                        punchayath_sl_no=no,
                        created_by=request.user
                    )
        except Exception as e:
            print(e)
        return HttpResponse("File uploaded successfully")
    return HttpResponse("Invalid request")


def deployapp(request):
    if request.method == 'POST':
        if User.objects.filter(is_superuser=True).exists():
            return HttpResponse("Application already deployed.")
        form = AdminUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            create_squads(user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Form is invalid.")
    return render(request, '_deploy.html')