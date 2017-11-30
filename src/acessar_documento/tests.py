from django.test import TestCase, Client
from .models import Arquivos
import os


class TestDoc(TestCase):

    def setUp(self):
        self.c = Client()
        self.pdf = open('CartilhaCae.pdf', 'rb')
        self.data = {'title': 'cartilha', 'arquivo': self.pdf}
        self.c.post('/upload_file/', self.data)
        self.pdf.close()

    def test_upload_file(self):
        self.assertEquals(self.data['arquivo'],
                          Arquivos.objects.last().arquivo)
        self.assertEqual(self.data['title'], Arquivos.objects.last().title)

    def test_documentsAll(self):
        response = self.c.get('/documentsAll/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'documentsAll.html')
        self.assertContains(response, 'CartilhaCae.pdf')
        self.assertNotContains(response, '.Ds_Store')

    def test_upload_file_template(self):
        response = self.c.get('/upload_file/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'Base.html')
        self.assertTemplateUsed(response, 'upload_file.html')

    def test_viewpdf(self):
        response = self.c.get('/viewpdf/CartilhaCae.pdf', follow=True)
        self.assertEquals(200, response.status_code)
        self.assertTrue(self.pdf.closed)

    def tearDown(self):
        os.remove('media/CartilhaCae.pdf')
