from django.test import TestCase, Client
from agendar_reuniao.models import Agendamento
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

    def test_index_schedule_post(self):
        self.client.force_login(self.user)
        
        self.assertEqual(self.data1['local'], Agendamento.objects.last().local)
        self.assertEqual(self.data1['time'],
                         Agendamento.objects.last().horario)
        self.assertEqual(self.data1['date'], Agendamento.objects.last().data)
        self.assertEqual(self.data1['note'],
                         Agendamento.objects.last().observacoes)
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'scheduled.html')

    def test_edit_schedule(self):
        logged_in = self.cliente.login(username='testuser', password='12345')

        self.assertEquals(logged_in, True)

    def test_template_edit_visit(self):
        self.cliente.login(username='testuser', password='12345')
        response = self.cliente.get('/editVisit/1')

        self.assertEquals(301, response.status_code)

    def test_template_indexScheduleMeeting(self):
        response = self.cliente.get('/indexScheduleMeeting/')

        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'indexScheduleMeeting.html')
        self.assertEquals(200, response.status_code)

    def test_template_schedules(self):
        response = self.cliente.get('/schedules/')

        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'schedules.html')
        self.assertEquals(200, response.status_code)

    def test_escheduled(self):
        self.cliente.login(username='testuser', password='12345')
        response = self.cliente.get('/scheduled/')

        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'scheduled.html')
        self.assertEquals(200, response.status_code)

    def test_save(self):
        data = '22/10/2017'
        local = 'teste'
        horario = '22:00'
        tema = 'teste'
        observacoes = 'teste function'
        nome_cae = 'CAE test'
        novo_agendamento = Agendamento()
        novo_agendamento.data = data
        novo_agendamento.local = local
        novo_agendamento.horario = horario
        novo_agendamento.tema = tema
        novo_agendamento.observacoes = observacoes
        novo_agendamento.nome_cae_schedule = nome_cae
        novo_agendamento.save()
        test_agendamento = Agendamento.objects.get(nome_cae_schedule=nome_cae)
        self.assertEquals(data, test_agendamento.data)
        self.assertEquals(local, test_agendamento.local)
        self.assertEquals(horario, test_agendamento.horario)
        self.assertEquals(tema, test_agendamento.tema)
        self.assertEquals(observacoes, test_agendamento.observacoes)
        self.assertEquals(nome_cae, test_agendamento.nome_cae_schedule)
        



