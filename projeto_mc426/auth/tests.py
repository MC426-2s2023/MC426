from django.test import TestCase
from django.test.testcases import ValidationError
from auth import forms
from parameterized import parameterized
from .forms import CreateUserForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

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
        #Usuário Válido = Sim, Senha Válida = Sim
        logged_in = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(logged_in)

    def test_authenticate_invalid_username(self):
        #Usuário Válido = Não, Senha Válida = Sim
        logged_in = self.client.login(username='wronguser', password='testpassword')
        self.assertFalse(logged_in)

    def test_authenticate_invalid_password(self):
        #Usuário Válido = Sim, Senha Válida = Não
        logged_in = self.client.login(username='testuser', password='wrongpassword')
        self.assertFalse(logged_in)

    def test_authenticate_invalid_username_password(self):
        #Usuário Válido = Não, Senha Válida = Não
        logged_in = self.client.login(username='wronguser', password='wrongpassword')
        self.assertFalse(logged_in)

class UserPositionTest(TestCase):
    def assertNotRaises(self,error, function, *args):
        try:
            function(*args)
            assert True
        except error:
            assert False

    def test_user_with_expected_lat_lng(self):
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        self.assertNotRaises(ValidationError, user.location_profile.setLatLng, 47, 120)

    def test_user_with_lat_greater_than_90(self):
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        self.assertRaises(ValidationError, user.location_profile.setLatLng, 91, 0)

    def test_user_with_lat_less_than_negative_90(self):
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        self.assertRaises(ValidationError, user.location_profile.setLatLng, -91, 0)

    def test_user_with_lng_greater_than_180(self):
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        self.assertRaises(ValidationError, user.location_profile.setLatLng, 0, 181)

    def test_user_with_lng_greater_than_negative_181(self):
        user = User.objects.create_user("nome_usuario", "email@a.com", "senha")
        self.assertRaises(ValidationError, user.location_profile.setLatLng, 0, -181)

class UserFormTest(TestCase):
    def test_user_with_151_characters(self):
        #Tamanho logo acima do limite superior
        dic = {
            'username': 'Este_usuario_esta_identificado_como_um_usuario_de_151_caracteres_superando_o_valor_o_limite_estabelecido_de_no_maximo_150_._Assim_devemos_ter_um_erro_.',
            'email': 'test1@example.com',
            'first_name': 'Monkey',
            'last_name': 'D Luffy',
            'password1': 'fljsdlf81',
            'password2': 'fljsdlf81'
        }
        form = CreateUserForm(dic)
        self.assertFalse(form.is_valid())
    
    def test_user_with_150_characters(self):
        #Testa limite superior do tamanho do usuario
        dic = {
            'username': 'Este_usuario_esta_identificado_como_um_usuario_de_150_caracteres_igualando_o_valor_o_limite_estabelecido_._Assim_nao_devemos_ter_um_erro_no_registro_.',
            'email': 'test1@example.com',
            'first_name': 'Monkey',
            'last_name': 'D Luffy',
            'password1': 'fljsdlf81',
            'password2': 'fljsdlf81'
        }
        form = CreateUserForm(dic)
        self.assertTrue(form.is_valid())
    
    def test_user_with_1_character(self):
        #Testa limite inferior do tamanho do usuario
        dic = {
            'username': '.',
            'email': 'test1@example.com',
            'first_name': 'Monkey',
            'last_name': 'D Luffy',
            'password1': 'fljsdlf81',
            'password2': 'fljsdlf81'
        }
        form = CreateUserForm(dic)
        self.assertTrue(form.is_valid())
    
class PasswordTest(TestCase): 

    def test_password_correct_pass(self):
        #Testa se a senha está da forma correta
        dic = {
            'username': 'testuser1',
            'email': 'test1@example.com',
            'first_name': 'Monkey',
            'last_name': 'D Luffy',
            'password1': 'fljsdlf81',
            'password2': 'fljsdlf81'
        }
        form = CreateUserForm(dic)
        self.assertTrue(form.is_valid())
        
    def test_password_similar_to_informations(self):
        #Testa se a senha é parecida com o restante das informações
        dic = {
            'username': 'testuser1',
            'email': 'test1@example.com',
            'first_name': 'Monkey',
            'last_name': 'D Luffy',
            'password1': 'testuser1',
            'password2': 'testuser1'
        }
        form = CreateUserForm(dic)
        self.assertFalse(form.is_valid())

    def test_password_with_8_characters(self):
        #Testa limite inferior do tamanho da senha
        dic = {
            'username': 'testuser1',
            'email': 'test1@example.com',
            'first_name': 'Monkey',
            'last_name': 'D Luffy',
            'password1': 'onepiece',
            'password2': 'onepiece'
        }
        form = CreateUserForm(dic)
        self.assertFalse(form.is_valid())
    
    def test_password_ordinary(self):
        #Testa se a senha é muito comum
        dic = {
            'username': 'testuser1',
            'email': 'test1@example.com',
            'first_name': 'Monkey',
            'last_name': 'D Luffy',
            'password1': 'a12345678',
            'password2': 'a12345678'
        }
        form = CreateUserForm(dic)
        self.assertFalse(form.is_valid())
        
    def test_password_with_only_numbers(self):
        #Testa se a senha é inteiramente numérica
        dic = {
            'username': 'testuser1',
            'email': 'test1@example.com',
            'first_name': 'Monkey',
            'last_name': 'D Luffy',
            'password1': '314159265',
            'password2': '314159265'
        }
        form = CreateUserForm(dic)
        self.assertFalse(form.is_valid())