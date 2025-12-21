from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import ListView
from core.models import Home

# Create your views here.


class Login(LoginView):
    template_name = 'sign-in.html'


class Home(LoginRequiredMixin, ListView):
    model = Home
    context_object_name = 'homes'
    template_name = '_home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = context['homes'].count()
        return context