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
        self.assertEquals(logged_in , True)
