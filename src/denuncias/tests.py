from django.test import TestCase, Client


class TestViews(TestCase):

    def setUp(self):
        self.c = Client()

    def test_denunciations(self):
        data = {
            'escola': 'fiscae',
            'cidade': 'brasilia',
            'estado': 'DF',
            'endereco': 'endereco_test',
            'subject': 'testando denuncias',
            'description': 'realizando testes das denuncias',
        }
        response = self.c.post('/denunciations/', data)
        self.assertEquals(200, response.status_code)

    def test_denuncias(self):
        self.assertTemplateUsed('denuncias/denunciations.html')
        self.assertTemplateUsed('Base.html')
