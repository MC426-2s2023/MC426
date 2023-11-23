from django.db import models
from django.conf import settings

# Create your models here.
class tipo_de_ocorrencia(models.Model):
    tdo_id = models.BigAutoField(primary_key=True)
    tdo_nome = models.CharField(max_length=255)
    tdo_peso = models.IntegerField()

class registro_de_ocorrencia(models.Model):
    rdo_id = models.BigAutoField(primary_key=True)
    rdo_tdo = models.ForeignKey(
        tipo_de_ocorrencia, on_delete=models.CASCADE
    )
    rdo_cep = models.CharField("CEP", max_length=50)
    rdo_rua = models.CharField("Rua", max_length=100)
    rdo_bairro = models.CharField("Bairro", max_length=50)
    rdo_cidade = models.CharField("Cidade", max_length=50)
    rdo_estado = models.CharField("Estado", max_length=50)
    rdo_numero = models.IntegerField("Número")
    rdo_dtocorrencia = models.DateField("Data da Ocorrência")
    rdo_hrocorrencia = models.TimeField("Hora da Ocorrência")