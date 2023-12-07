from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.crimeRegisterPage, name='crime_register'),
]
