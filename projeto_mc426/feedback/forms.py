from django import Forms

from .models import Feedback

class FeedbackForm(forms.modelForm):
    class Meta:
        model = Feedback
        fields = [email, title, description]
