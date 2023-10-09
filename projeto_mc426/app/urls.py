from django.urls import path
from . import views

urlpatterns = [
    path('auth/register/', views.registerPage, name='register'),
    path('auth/login/', views.loginPage, name='login'),
    path('home/', views.homePage, name='home'),
]
