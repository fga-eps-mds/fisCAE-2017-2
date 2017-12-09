from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Advisor
from django.contrib.auth import authenticate
from .forms import PresidentForm, AdministratorForm, AdvisorForm


class TestSimpleViews(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_login_page(self):
        response = self.c.get('/login/')
        self.assertEquals(200, response.status_code)

    def test_get_register_page(self):
        response = self.c.get('/registro/')
        self.assertEquals(200, response.status_code)

    def test_erro(self):
        response = self.c.get('/dontexist')
        self.assertEquals(404, response.status_code)

    def test_template(self):
        response = self.c.get('/login/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'login.html')
        response = self.c.get('/registro/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'registro.html')

    def test_templateNotExist(self):
        response = self.c.get('/registro/')
        self.assertTemplateNotUsed(response, 'notexist.html')


class TestForms(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test',
                                             password='123456')
        self.user.save()

    def test_register_user(self):
        data = {
            'username': 'fiscae',
            'password': 'fiscae',
            'user_type': 'advisor',
            'email': 'fiscae@hotmail.com',
            'name': 'fisCAE',
            'cpf': '7777777',
            'tipo_cae': 'Municipal',
            'cep': '7777777',
            'bairro': 'hhh',
            'municipio': 'goiania',
            'uf': 'go',
            'user_type': 'advisor'
        }

        self.c.post('/registro/', data)
        self.assertEquals(data['username'], User.objects.last().username)
        self.assertNotEquals(data['password'], User.objects.last().password)
        # a função padrão de senha do django crptografa a senha
        self.assertEquals(data['email'], Advisor.objects.last().email)
        self.assertEquals(data['name'], Advisor.objects.last().name)
        self.assertEquals(data['cpf'], Advisor.objects.last().cpf)
        self.assertEquals(data['tipo_cae'], Advisor.objects.last().tipo_cae)
        self.assertEquals(data['cep'], Advisor.objects.last().cep)
        self.assertEquals(data['bairro'], Advisor.objects.last().bairro)
        self.assertEquals(data['municipio'], Advisor.objects.last().municipio)
        self.assertEquals(data['uf'], Advisor.objects.last().uf)
        self.assertNotEquals(data['email'], Advisor.objects.last().uf)

    def test_authenticate_user(self):
        data = {'username': 'test', 'password': '123456'}
        response = self.c.post('/login/', data, follow=True)
        self.assertEquals(response.context['user'], self.user)
        self.c.logout()
        data = {'username': 'test', 'password': '12345'}
        response = self.c.post('/login/', data, follow=True)
        self.assertNotEquals(response.context['user'], self.user)
        self.c.logout()
        data = {'username': 'tes', 'password': '123456'}
        response = self.c.post('/login/', data, follow=True)
        self.assertNotEquals(response.context['user'], self.user)

    def test_register_DuplicateUser(self):
        data1 = {
            'username': 'robin',
            'password': 'testing',
            'email': 'jjj@ggg.com',
            'name': 'Test',
            'cpf': 'Tester',
            'tipo_cae': 'Municipal',
            'phone': '',
            'cep': '2223335555',
            'descricao': '',
            'bairro': 'sss',
            'municipio': 'goiania',
            'uf': 'go',
            'user_type': 'advisor',

        }
        data2 = {
            'username': 'robin',
            'password': 'testi',
            'email': 'hhh@ggg.com',
            'name': 'batma',
            'cpf': 'Tester',
            'tipo_cae': 'Municipal',
            'phone': '',
            'cep': '2223345555',
            'descricao': '',
            'bairro': 'sss',
            'municipio': 'goiania',
            'uf': 'go',
            'user_type': 'advisor',

        }
        self.c.post('/registro/', data1)
        response = self.c.post('/registro/', data2)
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'registro.html')
        self.assertContains(response, 'Registro inválido!')

    def test_logout_user(self):
        self.c.login(username='test', password='123456')
        response = self.c.get('/logout/')
        self.assertEquals(response.status_code, 302)

    def test_edit_user(self):
        # user = authenticate(username='test', password='123456')
        response = self.c.get('/userEdit/')
        self.assertEquals(302, response.status_code)

    def test_PresidentForm_valid(self):
        data = {
            'name': 'President Test',
            'email': 'president_test@email.com',
            'username': 'president_test',
            'password': 'president'
        }
        form = PresidentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_PresidentForm_invalid(self):
        data = {
            'name': 'President Test',
            'email': '',
            'username': 'president_test',
            'password': 'president'
        }
        form = PresidentForm(data=data)
        self.assertFalse(form.is_valid())

    def test_AdministratorForm_valid(self):
        data = {
            'name': 'President Test',
            'email': 'president_test@email.com',
            'username': 'president_test',
            'password': 'president'
        }
        form = AdministratorForm(data=data)
        self.assertTrue(form.is_valid())

    def test_AdministratortForm_invalid(self):
        data = {
            'name': 'Admin Test',
            'email': '',
            'username': 'admin_test',
            'password': 'admin'
        }
        form = AdministratorForm(data=data)
        self.assertFalse(form.is_valid())

    def test_AdvisorForm_valid(self):
        data = {
            'username': 'robin',
            'password': 'testing',
            'email': 'jjj@ggg.com',
            'name': 'Test',
            'cpf': 'Tester',
            'tipo_cae': 'Municipal',
            'cep': '2223335555',
            'bairro': 'sss',
            'municipio': 'goiania',
            'uf': 'go',
            'user_type': 'advisor',
        }
        form = AdvisorForm(data=data)
        self.assertTrue(form.is_valid())

    def test_AdvisorForm_invalid(self):
        data = {
            'username': 'robin',
            'password': '',
            'email': 'jjj@ggg.com',
            'name': 'Test',
            'cpf': 'Tester',
            'tipo_cae': 'Municipal',
            'cep': '',
            'bairro': 'sss',
            'municipio': 'goiania',
            'uf': 'go',
            'user_type': 'advisor',
        }
        form = AdvisorForm(data=data)
        self.assertFalse(form.is_valid())
