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

    def test_template(self):
        response = self.c.get('/user/login/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')
        response = self.c.get('/user/registro/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'registro.html')

    def test_templateNotExist(self):
        response = self.c.get('/user/registro/')
        self.assertTemplateNotUsed(response, 'notexist.html')


class TestForms(TestCase):
    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username='test',
                                             password='123456')
        self.user.save()

    def test_register_user(self):
        data = {
            'username': 'algo',
            'password': '123456',
            'email': 'jjj@ggg.com',
            'name': 'Test',
            'cpf': '',
            'phone': '',
            'cep': '2223335555',
            'bairro': 'hhh',
            'descricao': '',
            'municipio': 'goiania',
            'uf': 'go',

        }

        self.c.post('/user/registro/', data)
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

    def test_authenticate_user(self):
        data = {'username': 'test', 'password': '123456'}
        response = self.c.post('/user/login/', data, follow=True)
        self.assertEquals(response.context['user'], self.user)
        self.c.logout()
        data = {'username': 'test', 'password': '12345'}
        response = self.c.post('/user/login/', data, follow=True)
        self.assertNotEquals(response.context['user'], self.user)
        self.c.logout()
        data = {'username': 'tes', 'password': '123456'}
        response = self.c.post('/user/login/', data, follow=True)
        self.assertNotEquals(response.context['user'], self.user)

    def test_register_DuplicateUser(self):
        data1 = {
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
        data2 = {
            'username': 'robin',
            'password': 'testi',
            'email': 'hhh@ggg.com',
            'name': 'batma',
            'cpf': 'Tester',
            'phone': '',
            'cep': '2223345555',
            'descricao': '',
            'bairro': 'sss',
            'municipio': 'goiania',
            'uf': 'go',

        }
        self.c.post('/user/registro/', data1)
        response = self.c.post('/user/registro/', data2)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'registroException.html')

    def test_logout_user(self):
        self.c.login(username='test', password='123456')
        response = self.c.get('/user/logout')
        self.assertEquals(response.status_code, 301)
