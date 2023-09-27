from django.shortcuts import render

def register(request):
    return render(request, 'users/register.html')

def login(request):
    if request.method == "GET":
        return render(request, 'users/login.html')
    else:
        return
        