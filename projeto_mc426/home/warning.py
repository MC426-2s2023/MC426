from .models import registro_de_ocorrencia
from webpush import send_user_notification
from geopy import distance 

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

class Warning:
    def setMsg(self, msg_head, msg_body):
        self.msg = {
            "head": msg_head,
            "body": msg_body,
        }

    def warnUser(self, request, userPosition):
        radius = 20
        regProx = crimeRegisterProximity(userPosition[0], userPosition[1], radius)
        if regProx: # lista nao existe alguma ocorrencia
            self.setMsg("Atencao!",  "Existe uma ocorrencia ha " + regProx[0][1] + "metros" )
            send_user_notification(user=request.user, payload=self.msg, ttl=1000)
        return

    def update(self, request, lat, lng):
        self.warnUser(request, [lat, lng])     

