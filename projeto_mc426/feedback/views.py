from django.shortcuts import render
from django.http import HttpResponse

from .forms import FeedbackForm

# Create your views here.
def index(request):
    if (request.method == 'POST'):
        form = FeedbackForm(request.POST)
        if form.is_valid():
           form.save()
           return render(request, "feedback/agradecimento.html")
    else:
        form = FeedbackForm()
    return render(request, "feedback/formulario.html", {'form': form})
