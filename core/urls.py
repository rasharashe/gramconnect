from django.urls import path
from django.http import HttpResponse
from .views import Login, Home

urlpatterns = [
    path('signin/', Login.as_view(), name='signin'),
    path('home/', Home.as_view(), name='home'),
]