from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from feedback.models import Feedback
from feedback.forms import FeedbackForm

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
   
    def test_can_access_feedback_site_while_authenticated(self):
        """
        O usuário logado consegue acessar site de feedback diretamente.
        """
        User = get_user_model()
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        self.client.login(username="nome_usuario", password="senha")
        response = self.client.get(reverse("feedback:feedback"), follow=True)
        self.assertEqual(response.status_code, 200)
        # 200: requisição bem sucedida

class FeedbackFormTest(TestCase):
    def test_title_with_81_characters(self):
        User = get_user_model()
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        feedback = Feedback(user=user, pub_date=timezone.now(), answer="")
        data = {
            'title': "esse título tem oitenta e um caracteres Lorem ipsum dolo"
                     "r sit amet, consectetur a",
            'description': "descrição"
        }
        form = FeedbackForm(data, instance=feedback)
        self.assertFalse(form.is_valid())

    def test_title_with_80_characters(self):
        User = get_user_model()
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        feedback = Feedback(user=user, pub_date=timezone.now(), answer="")
        data = {
            'title': "Esse título tem oitenta caracteres Lorem ipsum dolor sit"
                     " amet, consectetur adipi",
            'description': "descrição"
        }
        form = FeedbackForm(data, instance=feedback)
        self.assertTrue(form.is_valid())
    
    def test_title_with_1_character(self):
        User = get_user_model()
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        feedback = Feedback(user=user, pub_date=timezone.now(), answer="")
        data = {
            'title': "a",
            'description': "descrição"
        }
        form = FeedbackForm(data, instance=feedback)
        self.assertTrue(form.is_valid())

    def test_title_with_0_characters(self):
        User = get_user_model()
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        feedback = Feedback(user=user, pub_date=timezone.now(), answer="")
        data = {
            'title': "",
            'description': "descrição"
        }
        form = FeedbackForm(data, instance=feedback)
        self.assertFalse(form.is_valid())