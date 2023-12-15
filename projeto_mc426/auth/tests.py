from django.test import TestCase
from auth import forms
from parameterized import parameterized
from .forms import CreateUserForm

class CreateUserFormTest(TestCase):
    @parameterized.expand([
        ("Valid User", {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Alice',
            'last_name': 'Maravilha',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }, True),
        ("Short Password", {
            'username': 'testuser',
            'email': 'test@example.com',
            'first_name': 'Bob',
            'last_name': 'Construtor',
            'password1': 'short',
            'password2': 'short'
        }, False),
        ("Invalid Email", {
            'username': 'testuser',
            'email': 'invalid_email',
            'first_name': 'Alice',
            'last_name': 'Maravilha',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }, False),
        ("Weak Password and Invalid Email", {
            'username': 'testuser',
            'email': 'invalid_email',
            'first_name': 'Bob',
            'last_name': 'Construtor',
            'password1': 'weak',
            'password2': 'weak'
        }, False),
    ])
    def test_create_user_form(self, name, data, expected_result):
        form = CreateUserForm(data)
        result = form.is_valid()
        with self.subTest(name=name):
            self.assertEqual(result, expected_result)

class UserAuthenticationTest(TestCase): #testa autenticação
    def setUp(self):
        self.user = forms.User.objects.create_user('testuser', 'test@example.com', 'testpassword')

    def test_authenticate_valid_user(self):
        logged_in = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(logged_in)

    def test_authenticate_invalid_user(self):
        logged_in = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(logged_in)