from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# OneToOne link para usuario padrao do Django
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_lat = models.DecimalField("latitude", max_digits=10, decimal_places=6)
    user_lng = models.DecimalField("longitude", max_digits=10, decimal_places=6)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

 
