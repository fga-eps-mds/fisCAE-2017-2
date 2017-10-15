from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Advisor


class TestSimpleViews(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_login_page(self):
        response = self.c.get('/user/login/')
        self.assertEquals(200, response.status_code)

    def test_get_register_page(self):
        response = self.c.get('/user/registro/')
        self.assertEquals(200, response.status_code)

    def test_erro(self):
        response = self.c.get('/user/dontexist')
        self.assertEquals(404, response.status_code)

    def test_templateLogin(self):
        response = self.c.get('/user/login/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')

    def test_templateRegistro(self):
        response = self.c.get('/user/registro/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'registro.html')

    def test_templateNotExist(self):
        response = self.c.get('/user/registro/')
        self.assertTemplateNotUsed(response, 'notexist.html')


class TestForms(TestCase):

    def test_register_user(self):
        data = {
            'username': 'robin',
            'password': 'testing',
            'email': '',
            'name': 'Test',
            'cpf': 'Tester',
            'phone': '',
            'cep': '2223335555',
            'descricao': '',
            'bairro': 'sss',
            'municipio': 'goiania',
            'uf': 'go',

        }
        c = Client()
        c.post('/user/registro/', data)
        self.assertEquals(data['username'], User.objects.last().username)
        self.assertEquals(data['email'], Advisor.objects.last().email)
