from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.core import serializers
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


userPosition = None

# executar periodicamente
def getUserPosition():
    
    # if userPosition changed  
    # warnUser()
    pass

def getPointsDist(ptA, ptB):
    return distance.distance(ptA[:2], ptB[:2]).m

def crimeRegisterProximity(lat, lng, radius):
    ptA = [lat, lng]
    regs = registro_de_ocorrencia.objects.all()

    crime_regs = []
    for reg in regs:
        dist = getPointsDist(ptA, [reg.rdo_lat, reg.rdo_lng])
        if dist <= radius:
            crime_regs.append((reg.id, dist))

    return crime_regs.sort(key= lambda vector: vector[1])

def warnUser(request, userPosition):
    radius = 20
    regProx = crimeRegisterProximity(userPosition[0], userPosition[1], radius)
    if regProx: # lista nao existe alguma ocorrencia
        msg = {"head": "Atencao!", "body": "Existe uma ocorrencia ha " + regProx[0][1] + "metros" }
        send_user_notification(user=request.user, payload=msg, ttl=1000)
    return

