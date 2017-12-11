from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User


class EditScheduleTest(TestCase):
    def setUp(self):
        self.cliente = Client()

    def teste_template_edit_visit(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.cliente.login(username='testuser', password='12345')
        response = self.cliente.get('/editVisit/1')
        self.assertEquals(301, response.status_code)

    def teste_template_indexScheduleVisit(self):
        response = self.cliente.get('/indexScheduleVisit/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'indexScheduleVisit.html')
        self.assertEquals(200, response.status_code)
