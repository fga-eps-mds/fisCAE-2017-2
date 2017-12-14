from django.test import TestCase
from nuvem_civica.services import authenticateUser, postUser
import requests
import json


class NuvemTest(TestCase):

    # CUIDADO AO DESCOMENTAR E RODAR ESTE TESTE!!!!
    # ele está acessando a nuvem civica  e quebrando ela
    def test_autenticateUser(self):
        email = 'fiscae@hotmail.com'
        password = 'fiscae'

        url_base = 'http://mobile-aceite.tcu.gov.br:80/appCivicoRS'
        rest = '/rest/pessoas/autenticar?'
        url = url_base + rest

        headers = {'email': email, 'senha': password}
        request = requests.get(url, headers=headers)

        text = json.loads(request.text)
        header = request.headers
        dictionary = {'request': request, 'text': text, 'header': header}
        response = authenticateUser(email, '123456')
        self.assertEquals(dictionary['request'].status_code, 200)
        self.assertEquals(response['request'].status_code, 401)

    def test_postUser(self):
        url = 'http://mobile-aceite.tcu.gov.br:80/appCivicoRS/rest/pessoas/'
        cep = '70430107'
        email = 'jose@gmail.com'
        name = 'jose'
        username = 'Teste'
        password = '123456'
        data = {
            'CEP': cep,
            'email': email,
            'nomeCompleto': name,
            'nomeUsuario': username,
            'senha': password,
            'sexo': 'F',
            "tokenFacebook": "",
            "tokenGoogle": "",
            "tokenInstagram": "",
            "tokenTwitter": ""
        }
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        response = requests.post(url, data=json.dumps(data), headers=headers)
        response1 = postUser(cep, email, name, username, password)
        self.assertEqual(response.status_code, response1.status_code)
