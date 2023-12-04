from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from register.forms import registro_de_ocorrenciaForm
from decimal import Decimal
from home.models import *
import requests
# Create your views here.

@login_required
def crimeRegisterPage(request):
    if request.method == 'POST':
        rdo_rua = request.POST.get("rdo_rua")
        rdo_bairro = request.POST.get("rdo_bairro")
        rdo_cidade = request.POST.get("rdo_cidade")
        rdo_estado = request.POST.get("rdo_estado")
        rdo_numero = request.POST.get("rdo_numero")
        
        #consulta a API do openstreetmap para pegar a latitutde e longitude
        query = f'{rdo_rua}+{rdo_bairro}+{rdo_cidade}+{rdo_estado}+{rdo_numero}'

        params = {
            'format': 'json',
            'q': query
        }
        response = requests.get('https://nominatim.openstreetmap.org/search', params=params)

        if response.status_code == 200:
            data = response.json()
            lat = data[0]['lat']
            lng = data[0]['lon']

        registro = registro_de_ocorrencia(
            # rdo_id = 42,
            rdo_tdo = tipo_de_ocorrencia(
                #tdo_id = 54,
                tdo_nome = "Crime",
                tdo_peso = 10
            ),
            rdo_cep = request.POST.get("rdo_cep"),
            rdo_rua = request.POST.get("rdo_rua"),  
            rdo_bairro = request.POST.get("rdo_bairro"),
            rdo_cidade = request.POST.get("rdo_cidade"),
            rdo_estado = request.POST.get("rdo_estado"),
            rdo_numero = request.POST.get("rdo_numero"),
            rdo_lat = lat,
            rdo_lng = lng,
            rdo_dtocorrencia =  timezone.now().date(),
            rdo_hrocorrencia = timezone.now().time(),
        )
        # SE QUISER APAGAR TESTES
        # i = 9
        # while i >= 4:
        #     apagar = registro_de_ocorrencia.objects.get(rdo_id = i)
        #     apagar.delete()
        #     i -= 1
        form = registro_de_ocorrenciaForm(request.POST, instance=registro)
        if form.is_valid(): # SÓ VAI ATÉ O ID 3, POR ENQUANTO (3ª OPÇAO DE CRIME)
            form.save()
            return render(request, 'crime_register_agradecimento.html')
        
    else:
        form = registro_de_ocorrenciaForm()
    return render(request, 'crime_register.html', {'form': form})
    
