from django.test import TestCase, Client


class TestSimpleViews(TestCase):

    def setUp(self):
        self.c = Client()

    def test_get_login_page(self):
        response = self.c.get('/user/login/')
        self.assertEquals(200, response.status_code)

    def test_get_register_page(self):
        response = self.c.get('/user/registro/')
        self.assertEquals(200, response.status_code)

    def test_erro(self):
        response = self.c.get('/user/dontexist')
        self.assertEquals(404, response.status_code)

    def test_templateLogin(self):
        response = self.c.get('/user/login/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'login.html')

    def test_templateRegistro(self):
        response = self.c.get('/user/registro/')
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'registro.html')

    def test_templateNotExist(self):
        response = self.c.get('/user/registro/')
        self.assertTemplateNotUsed(response, 'notexist.html')

    
