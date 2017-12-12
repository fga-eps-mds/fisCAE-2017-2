from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .models import ScheduleVisit


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

    def teste_template_edit_visit(self):
        self.cliente.login(username='testuser', password='12345')
        response = self.cliente.get('/editar-visita/1')
        self.assertEquals(301, response.status_code)

    def teste_template_indexScheduleVisit(self):
        response = self.cliente.get('/agendar-visita/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'indexScheduleVisit.html')
        self.assertEquals(200, response.status_code)

    def test_save_visit(self):
        school_name = 'escola teste'
        school_code = '123456'
        data = '12/12/2018'
        horario = '12:12'
        membros = 'todos'
        estado = False
        nome_cae = 'teste'
        novo_agendamento = ScheduleVisit()
        novo_agendamento.schoolName = school_name
        novo_agendamento.schoolCode = school_code
        novo_agendamento.date = data
        novo_agendamento.time = horario
        novo_agendamento.members = membros
        novo_agendamento.status = estado
        novo_agendamento.nome_cae_schedule = nome_cae
        novo_agendamento.save()
        test_agendamento = ScheduleVisit.objects.get(
                            nome_cae_schedule=nome_cae)

        self.assertEquals(school_name, test_agendamento.schoolName)
        self.assertEquals(school_code, test_agendamento.schoolCode)
        self.assertEquals(data, test_agendamento.date)
        self.assertEquals(horario, test_agendamento.time)
        self.assertEquals(membros, test_agendamento.members)
        self.assertEquals(estado, test_agendamento.status)
        self.assertEquals(nome_cae, test_agendamento.nome_cae_schedule)
    ''' def test_indexScheduleVisit_get(self):
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
        self.assertEqual(response.status_code, 200) '''
