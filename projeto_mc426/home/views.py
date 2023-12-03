from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.core import serializers
from .models import registro_de_ocorrencia
from webpush import send_user_notification
# Create your views here.

def homePage(request):
    data = registro_de_ocorrencia.objects.all()
    context = {
        "data": data
    }
    msg = {"head": "Welcome!", "body": "Hello World"}
    send_user_notification(user=request.user, payload=msg, ttl=1000)
    return render(request, 'home.html', context)
    #if request.user.is_authenticated:
    #    return render(request, 'home.html')
    #else:
    #    return redirect('../auth/login/')
