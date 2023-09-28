from django.db import models

# Create your models here.
class Feedback(models.Model):
    email = models.EmailField("E-Mail")
    title = models.CharField("Título", max_length=80)
    description = models.TextField("Descrição")
    date = models.DateTimeField("Data de publicação")
