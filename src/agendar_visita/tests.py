from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from .models import ScheduleVisit


class EditScheduleTest(TestCase):
    def setUp(self):
        self.cliente = Client()

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
