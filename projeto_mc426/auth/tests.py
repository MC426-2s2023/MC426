from django.test import TestCase
from django.urls import reverse
from auth import forms

class UserCreationTest(TestCase): #testa a criação de usuário
    def testCreateUser(self):
        forms.User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.assertEqual(forms.User.objects.count(), 1)

class UserAuthenticationTest(TestCase): #testa autenticação
    def setUp(self):
        self.user = forms.User.objects.create_user('testuser', 'test@example.com', 'testpassword')

    def test_authenticate_valid_user(self):
        logged_in = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(logged_in)

    def test_authenticate_invalid_user(self):
        logged_in = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(logged_in)