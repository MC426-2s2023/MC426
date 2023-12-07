from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('feedback/', include('feedback.urls')),
]
