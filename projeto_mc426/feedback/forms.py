from django import forms

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'description']

class FeedbackAnswerForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['answer']