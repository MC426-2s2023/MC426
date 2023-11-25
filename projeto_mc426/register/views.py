from django.shortcuts import render

# Create your views here.

def crimeRegisterPage(request):
    return render(request, 'crime_register.html')
    #if request.user.is_authenticated:
    #    return render(request, 'home.html')
    #else:
    #    return redirect('../auth/login/')