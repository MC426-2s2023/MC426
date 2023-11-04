from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class FeedbackTests(TestCase):
    def test_cannot_access_feedback_site_without_authentication(self):
        """
        O usuário deve estar logado para acessar site de feedback.
        """
        response = self.client.get(reverse("feedback:feedback"))
        self.assertEqual(response.status_code, 302) 
        # 302: redirecionamento temporário
        self.assertURLEqual(
            response.url,
            reverse("login")[:-1] + "?next=" + reverse("feedback:feedback")
        )
