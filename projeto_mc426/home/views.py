from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from .models import registro_de_ocorrencia
from webpush import send_user_notification
from geopy import distance 
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



# @ajax_required
def updateLocation(request):
    # try:
        if request.method == 'POST':
            lat = request.POST.get('lat')
            lng = request.POST.get('lng')
            if request.user.is_authenticated:
                request.user.location_profile.updateUserLocation(request, lat, lng)
            return redirect('/home')
    # except Exception:   
        # return HttpResponseBadRequest()



