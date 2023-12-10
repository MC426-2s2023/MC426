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
        self.assertRedirects(
            response,
            reverse("login") + "?next=" + reverse("feedback:feedback")
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
