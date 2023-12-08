from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from register.forms import registro_de_ocorrenciaForm
from decimal import Decimal
from home.models import *
import requests
# Create your views here.

def getLocationData(rua, bairro, cidade, estado, numero):
    query = f'{rua}+{bairro}+{cidade}+{estado}+{numero}'
    params = {'format': 'json', 'q': query}
    response = requests.get('https://nominatim.openstreetmap.org/search', params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0].get('lat'), data[0].get('lon')
    return None, None

@login_required
def crimeRegisterPage(request):
    if request.method == 'POST':
        form = registro_de_ocorrenciaForm(request.POST)

        if form.is_valid():
            registro_de_ocorrencia()
            cleaned_data = form.cleaned_data
            lat, lng = getLocationData(
                cleaned_data.get("rdo_rua"), 
                cleaned_data.get("rdo_bairro"),
                cleaned_data.get("rdo_cidade"), 
                cleaned_data.get("rdo_estado"),
                cleaned_data.get("rdo_numero")
            )

            if lat is not None and lng is not None:
                registro = form.save(commit=False)
                registro.rdo_lat = lat
                registro.rdo_lng = lng
                registro.rdo_dtocorrencia = timezone.now().date()
                registro.rdo_hrocorrencia = timezone.now().time()
                registro.save()
                return render(request, 'crime_register_agradecimento.html')
            else:
                form.add_error(None, 'Local não encontrado.')
                return render(request, 'crime_register_erro.html', {'form': form})
        return render(request, 'crime_register.html', {'form': form})
    else:
        form = registro_de_ocorrenciaForm()
    return render(request, 'crime_register.html', {'form': form})
    
