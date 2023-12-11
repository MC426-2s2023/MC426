from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.warning import Warning


# OneToOne link para usuario padrao do Django
class LocationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, related_name = "location_profile")
    user_lat = models.DecimalField("latitude", max_digits=10, decimal_places=6)
    user_lng = models.DecimalField("longitude", max_digits=10, decimal_places=6)
    subs = [Warning()]

    def subscribe(self, newSub):
        self.subs.append(newSub)

    def updateUserLocation(self, request, lat, lng):
        if self.user_lat == lat and self.user_lng == lng: # posicao nao foi alterada
            return

        self.user_lat, self.user_lng = lat,lng
        self.save(update_fields=['user_lat', 'user_lng'])

        for subscriber in self.subs:
            subscriber.update(request, lat, lng)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        LocationProfile.objects.create(user=instance, user_lat=0, user_lng=0)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.location_profile.save()

 
