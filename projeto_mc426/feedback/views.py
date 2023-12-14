from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import timezone

from .forms import FeedbackForm, FeedbackAnswerForm
from .models import Feedback

# Create your views here.
@login_required
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

@login_required
def detail(request, feedback_id):
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    return render(request, "feedback/feedback.html", {'feedback': feedback})

@login_required
def list(request):
    list = Feedback.objects.order_by('-pub_date')
    return render(request, 'feedback/list.html', {'list': list})

@staff_member_required
def answer(request, feedback_id):
    feedback = Feedback.objects.get(pk=feedback_id)
    if (request.method == 'POST'):
        form = FeedbackAnswerForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return render(request, "feedback/answer_sent.html", {'feedback': feedback})
    else:
        form = FeedbackAnswerForm()
    return render(request, "feedback/answer.html", {'feedback': feedback, 'form': form})