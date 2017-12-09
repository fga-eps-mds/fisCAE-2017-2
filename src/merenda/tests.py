from django.test import TestCase, Client


class merendaTest(TestCase):

    def test_notLoggedIn(self):
        c = Client()
        response = c.get('/notLoggedIn/')
        self.assertEqual(200, response.status_code)
