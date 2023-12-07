from django import forms

from home.models import *

class registro_de_ocorrenciaForm(forms.ModelForm):
    class Meta:
        model = registro_de_ocorrencia
        fields = ['rdo_tdo', 'rdo_cep','rdo_rua','rdo_bairro',
                  'rdo_cidade','rdo_estado','rdo_numero',]
        