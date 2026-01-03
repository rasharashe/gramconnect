from django.urls import path
from django.http import HttpResponse
from .views import Login, HomeList, SquadList, DashboardView, bulk_upload, deployapp

urlpatterns = [
    path('', Login.as_view(), name='signin'),
    path('home/', HomeList.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('upload/home/_bulk/', bulk_upload, name='home_bulk_upload'),
    path('deployapp/', deployapp, name='deploy_app'),
    path('squad/<str:sqid>/', SquadList.as_view(), name='squad_homes'),
]