from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

# Create your views here.

def homePage(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    else:
        return redirect('../auth/login/')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Conta foi criada para ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'users/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Usuário ou senha está incorreto.')
            return render(request, 'users/login.html')

    return render(request, 'users/login.html')
    
