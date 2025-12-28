from django.urls import path
from django.http import HttpResponse
from .views import Login, HomeList, SquadList, bulk_upload, deployapp

urlpatterns = [
    path('', Login.as_view(), name='signin'),
    path('home/', HomeList.as_view(), name='home'),
    path('upload/home/_bulk/', bulk_upload, name='home_bulk_upload'),
    path('deployapp/', deployapp, name='deploy_app'),
    path('squad/<str:sqid>/', SquadList.as_view(), name='squad_homes'),
]