from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .forms import FeedbackForm
from .models import Feedback

# Create your views here.
@login_required(login_url='/auth/login')
def index(request):
    if (request.method == 'POST'):
        feedback = Feedback(
            user = request.user,
            pub_date = timezone.now(),
            answer = "",
        )
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
           form.save()
           return render(request, "feedback/agradecimento.html")
    else:
        form = FeedbackForm()
    return render(request, "feedback/formulario.html", {'form': form})
