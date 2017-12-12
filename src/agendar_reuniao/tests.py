from django.test import TestCase, Client
from agendar_reuniao.models import Agendamento
from django.contrib.auth.models import User


class ScheduleTest(TestCase):

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
        'municipio': 'Brasilia',
        'uf': 'DF'}

    def setUp(self):
        self.cliente = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.user.save()
        self.advisor = self.client.post('/registro/', registro)
        self.client.force_login(self.user)
        self.agenda = Agendamento.objects.create(data='12/08',
                                                 horario='13:00',
                                                 local='gama',
                                                 tema='discussão',
                                                 observacoes='levem lanche',
                                                 nome_cae_schedule='newton')
        self.agenda.save

    def test_index_schedule_post(self):
        data = {
            'date': '22 de janeiro',
            'time': 'dez e vinte',
            'local': 'no parque',
            'note': 'levem lanche'
        }
        self.response = self.client.post('/agendar-reuniao/', data,
                                         follow=True)
        self.assertEqual(self.data['local'], Agendamento.objects.last().local)
        self.assertEqual(self.data['time'],
                         Agendamento.objects.last().horario)
        self.assertEqual(data['date'], Agendamento.objects.last().data)
        self.assertEqual(data['note'],
                         Agendamento.objects.last().observacoes)
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'scheduled.html')

    def test_edit_schedule_get(self):
        response = self.cliente.get(
            '/editar-reuniao/{}/'.format(self.agenda.pk))
        self.assertEqual(response.status_code, 302)

    def test_edit_schedule_post(self):
        data = {
            'data': '2/4',
            'horario': '22:00',
            'local': 'parque',
            'observacoes': '2 horas'
        }
        response = self.cliente.post(
            '/editar-reuniao/{}/'.format(self.agenda.pk), data)
        self.assertEqual(response.status_code, 302)

    def teste_template_indexScheduleMeeting(self):
        response = self.cliente.get('/agendar-reuniao/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'indexScheduleMeeting.html')
        self.assertEquals(200, response.status_code)

    def teste_template_schedules(self):
        response = self.cliente.get('/eventos/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'schedules.html')
        self.assertEquals(200, response.status_code)
