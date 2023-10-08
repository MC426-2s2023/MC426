from django.db import models
from django.conf import settings

# Create your models here.
class Feedback(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    title = models.CharField("Título", max_length=80)
    description = models.TextField("Descrição")
    pub_date = models.DateField("Data de publicação")
    answer = models.TextField("Resposta")
