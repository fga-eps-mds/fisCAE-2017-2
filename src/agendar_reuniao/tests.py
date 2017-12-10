from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from user.models import Advisor
from django.contrib.auth.models import User
from user.models import *


class EditScheduleTest(TestCase):
    def setUp(self):
        self.cliente = Client()

    def test_edit_schedule(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        logged_in = self.cliente.login(username='testuser', password='12345')
        self.assertEquals(logged_in, True)

    def teste_template_edit_visit(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        logged_in = self.cliente.login(username='testuser', password='12345')
        response = self.cliente.get('/editVisit/1')
        self.assertEquals(301, response.status_code)

    def teste_template_indexScheduleMeeting(self):
        response = self.cliente.get('/indexScheduleMeeting/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'indexScheduleMeeting.html')
        self.assertEquals(200, response.status_code)

    def teste_template_schedules(self):
        response = self.cliente.get('/schedules/')
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'schedules.html')
        self.assertEquals(200, response.status_code)

 
