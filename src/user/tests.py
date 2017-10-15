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
            'email': 'jjj@ggg.com',
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
        self.assertNotEquals(data['password'], User.objects.last().password)
        # a função padrão de senha do django crptografa a senha
        self.assertEquals(data['email'], Advisor.objects.last().email)
        self.assertEquals(data['name'], Advisor.objects.last().name)
        self.assertEquals(data['cpf'], Advisor.objects.last().cpf)
        self.assertEquals(data['phone'], Advisor.objects.last().phone)
        self.assertEquals(data['cep'], Advisor.objects.last().cep)
        self.assertEquals(data['descricao'], Advisor.objects.last().descricao)
        self.assertEquals(data['bairro'], Advisor.objects.last().bairro)
        self.assertEquals(data['municipio'], Advisor.objects.last().municipio)
        self.assertEquals(data['uf'], Advisor.objects.last().uf)
        self.assertNotEquals(data['email'], Advisor.objects.last().uf)
