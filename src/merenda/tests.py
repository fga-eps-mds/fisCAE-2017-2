from django.test import TestCase, Client


class merendaTest(TestCase):

    def test_notLoggedIn(self):
        c = Client()
        response = c.get('/acesso-negado/')
        self.assertEqual(200, response.status_code)

    def test_about(self):
        c = Client()
        response = c.get('/sobre/')
        self.assertEqual(200, response.status_code)
