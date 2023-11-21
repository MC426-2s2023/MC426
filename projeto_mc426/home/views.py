from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.

def homePage(request):
    return render(request, 'home.html')
    #if request.user.is_authenticated:
    #    return render(request, 'home.html')
    #else:
    #    return redirect('../auth/login/')
