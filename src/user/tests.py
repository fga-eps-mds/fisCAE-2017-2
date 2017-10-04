import unittest
from django.test import Client
from django.shortcuts import render
# Create your tests here


class usertest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def registertest(self, request):
        result = self.client.post('/user/registro', {'username': 'jhon111',
                                                     'name': 'jhon',
                                                     'email': 'jo@mail.com',
                                                     'cpf': '0000',
                                                     'cep': '333',
                                                     'bairro': 'limoeiro',
                                                     'municipio': 'goiania',
                                                     'password': '123456',
                                                     'uf': 'GO'})
        self.assertEqual(result, render(request, 'login.html'))

