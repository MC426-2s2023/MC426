from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.core import serializers
from .models import registro_de_ocorrencia
# Create your views here.

def homePage(request):
    data = registro_de_ocorrencia.objects.all()
    context = {
        "data": data
    }
    return render(request, 'home.html', context)
    #if request.user.is_authenticated:
    #    return render(request, 'home.html')
    #else:
    #    return redirect('../auth/login/')
