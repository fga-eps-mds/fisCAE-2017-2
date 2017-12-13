from django.test import TestCase
from nuvem_civica.services import authenticateUser
import requests
import json


class NuvemTest(TestCase):

    # CUIDADO AO DESCOMENTAR E RODAR ESTE TESTE!!!!
    # ele está acessando a nuvem civica  e quebrando ela
    ''' def test_autenticateUser(self):
        email = 'jjj@hotmail.com'
        password = '123456'

        url_base = 'http://mobile-aceite.tcu.gov.br:80/appCivicoRS'
        rest = '/rest/pessoas/autenticar?'
        url = url_base + rest

        headers = {'email': email, 'senha': password}
        request = requests.get(url, headers=headers)

        text = json.loads(request.text)
        header = request.headers
        dictionary = {'request': request, 'text': text, 'header': header}
        self.assertEquals(dictionary,
                          authenticateUser('jjj@hotmail.com', '123456')) '''
