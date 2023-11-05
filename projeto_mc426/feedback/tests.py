from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from feedback import forms

# Create your tests here.

class FeedbackAcessTests(TestCase):
    def test_cannot_access_feedback_site_without_authentication(self):
        """
        O usuário não logado é redirecionado ao site de login.
        """
        response = self.client.get(reverse("feedback:feedback"))
        self.assertEqual(response.status_code, 302) 
        # 302: redirecionamento temporário
        self.assertURLEqual(
            response.url,
            reverse("login")[:-1] + "?next=" + reverse("feedback:feedback")
        )
   
    def test_can_access_feedback_site_while_authenticaded(self):
        """
        O usuário logado consegue acessar site de feedback diretamente.
        """
        User = get_user_model()
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        self.client.login(username="nome_usuario", password="senha")
        response = self.client.get(reverse("feedback:feedback"), follow=True)
        self.assertEqual(response.status_code, 200)
        # 200: requisição bem sucedida

# class FeedbackCreationTest(TestCase):
#     def testCreateFeedback(self):
#         """
#         Verifica se o usuário consegue criar um feedback.
#         """
#         User = get_user_model()
#         user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
#         feedback = forms.Feedback.create(user = user, pub_date = timezone.now(), answer = "", 
#                                         title = "titulo_teste", description = "teste_feedback",)
#         form = forms.FeedbackForm(instance=feedback)
#         if form.is_valid():
#            form.save()
#         self.assertEqual(forms.Feedback.objects.count(), 1)
