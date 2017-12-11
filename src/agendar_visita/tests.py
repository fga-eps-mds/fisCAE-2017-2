from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class EditScheduleTest(TestCase):
    def setUp(self):
        self.cliente = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.user.save()
        data = {
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
            'municipio': 'Brasilia',
            'uf': 'DF'
        }
        self.advisor = self.client.post('/registro/', data)
        self.client.force_login(self.user)
        self.data1 = {
            'date': '22 de janeiro',
            'time': 'dez e vinte',
            'local': 'no parque',
            'note': 'levem lanche'
        }
        self.response = self.client.post(
            '/indexScheduleMeeting/', self.data1, follow=True)

    def test_edit_schedule(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        logged_in = self.cliente.login(username='testuser', password='12345')
        self.assertEquals(logged_in, True)

    def test_template_edit_visit(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        logged_in = self.cliente.login(username='testuser', password='12345')
        response = self.cliente.get('/editVisit/1')
        self.assertEquals(301, response.status_code)

    def test_template_indexScheduleVisit(self):
        response = self.cliente.get('/indexScheduleVisit/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'indexScheduleVisit.html')
        self.assertEquals(200, response.status_code)

    # def test_sceduled(self):
    #     self.cliente.login(username='testuser', password='12345')
    #     response = self.cliente.get('/visitScheduleds/')
    #     self.assertTemplateUsed(response, 'Base.html')
    #     self.assertTemplateUsed(response, 'visitScheduleds.html')
    #     self.assertEquals(200, response.status_code)
