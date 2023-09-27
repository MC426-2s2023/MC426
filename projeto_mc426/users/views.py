from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'users/register.html', context)

def login(request):
    if request.method == "GET":
        return render(request, 'users/login.html')
    else:
        return
        