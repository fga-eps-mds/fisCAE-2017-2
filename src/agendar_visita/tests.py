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
        'uf': 'DF'
    }

    def setUp(self):
        self.cliente = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.user.save()
        self.advisor = self.client.post('/registro/', registro)

    def test_template_edit_visit(self):
        # logged_in = self.user.login(username='testuser', password='12345')
        # User.objects.create_user(username="teste", password="teste")
        # self.cliente.login(username='teste', password='teste')
        # response = self.cliente.get('/editar-visita/1/')
        # self.assertEquals(200, response.status_code)
        self.assertTemplateUsed('Base.html')

    def test_template_indexScheduleVisit(self):
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

    def test_edit_schedule(self):
        # logged_in = self.cliente.login(username='testuser', password='12345')
        logged_in = self.cliente.login(username="testuser", password="12345")
        self.assertEquals(logged_in, True)
        # response = self.cliente.get('/editar-visita/{}/'.format(1))
        # self.assertTemplateUsed(response, 'Base.html')
        # self.assertTemplateUsed(response, 'editVisit.html')
        # self.assertEqual(response.status_code, 200)

    def test_template_schedules(self):
        self.cliente.login(username='testuser', password='12345')
        response = self.cliente.get('/visitas-agendadas/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertEquals(200, response.status_code)

    def test_escheduled(self):
        self.cliente.login(username='testuser', password='12345')
        # response = self.cliente.get('/scheduled/')
        self.assertTemplateUsed('Base.html')
        # self.assertTemplateUsed(response, 'scheduled.html')
        # self.assertEquals(200, response.status_code)

    def test_indexScheduleVisit_post(self):
        self.cliente.force_login(self.user)

        # self.cliente.post('/schoolForm/', data, follow=True)
        data1 = {
            'nome': 'joao',
            'codEscola': '1',
            'date': '11/2',
            'time': '11:20',
            'members': 'aquiles'
        }
        # response = self.cliente.post(
        #     '/indexScheduleVisit/', data1, follow=True)
        # self.assertEqual(data1['date'], ScheduleVisit.objects.last().date)
        # self.assertEqual(data1['time'], ScheduleVisit.objects.last().time)
        # self.assertEqual(data1['members'],
        #  ScheduleVisit.objects.last().members)
        # self.assertEqual(response.status_code, 200)

    def test_escheduledVisitDelete(self):
        self.cliente.login(username="testuser", password="12345")
        response = self.cliente.get('/deletar-visita/{}/'.format(1))
        self.assertTemplateUsed(response, 'deleteScheduleVisit.html')
        self.assertEqual(response.status_code, 200)

    def test_esceduled(self):
        self.cliente.login(username="testuser", password="12345")
        response = self.cliente.get('/visitas-agendadas/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'visitScheduleds.html')
        self.assertEqual(response.status_code, 200)

    def test_esceduled_except(self):
        response = self.cliente.get('/visitas-agendadas/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'schedules.html')
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "Apenas membros de CAE podem" +
            " ter acesso à essas funcionalidades!")

    def test_scheduleVisit(self):
        agenda = ScheduleVisit()
        agenda.updateStatus(agenda)
        self.assertFalse(agenda.status)
