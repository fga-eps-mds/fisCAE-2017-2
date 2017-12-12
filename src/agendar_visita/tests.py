from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .models import ScheduleVisit
from search_school.views import getFilteredItems


class EditScheduleTest(TestCase):
    global registro
    registro = {
        'username': 'test555',
        'password': '123456',
        'name': 'joao',
        'email': 'jj@asb.com',
        'cpf': '1234',
        'tipo_cae': 'Municipal',
        'user_type': 'advisor',
        'nome_cae': 'CAE',
        'cep': '72430107',
        'bairro': 'setor norte',
        'municipio': 'Brasília',
        'uf': 'DF'}

    def setUp(self):
        self.cliente = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.user.save()
        self.advisor = self.client.post('/registro/', registro)

    def test_template_edit_visit(self):
        self.cliente.login(username='testuser', password='12345')
        response = self.cliente.get('/editVisit/1')
        self.assertEquals(301, response.status_code)

    def test_template_indexScheduleVisit(self):
        response = self.cliente.get('/indexScheduleVisit/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'indexScheduleVisit.html')
        self.assertEquals(200, response.status_code)

    def test_indexScheduleVisit_get(self):
        self.cliente.force_login(self.user)

       # self.cliente.post('/schoolForm/', data, follow=True)
        data1 = {
            'nome': 'joao',
            'codEscola': '1',
            'date': '11/2',
            'time': '11:20',
            'members': 'aquiles'
        }
        response = self.cliente.post(
            '/indexScheduleVisit/', data1, follow=True)
        self.assertEqual(data1['date'], ScheduleVisit.objects.last().date)
        self.assertEqual(data1['time'], ScheduleVisit.objects.last().time)
        self.assertEqual(data1['members'],
                         ScheduleVisit.objects.last().members)
        self.assertEqual(response.status_code, 200)
