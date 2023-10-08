from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import FeedbackForm

# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    if (request.method == 'POST'):
        form = FeedbackForm(request.POST)
        if form.is_valid():
           form.save()
           return render(request, "feedback/agradecimento.html")
    else:
        form = FeedbackForm()
    return render(request, "feedback/formulario.html", {'form': form})
