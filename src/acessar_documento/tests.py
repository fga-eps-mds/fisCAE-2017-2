from django.test import TestCase, Client


class TestDoc(TestCase):

    def setUp(self):
        self.c = Client()

    def test_documentsAll(self):
        response = self.c.get('/documentsAll/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'base_docs.html')
        self.assertTemplateUsed(response, 'documentsAll.html')
        self.assertContains(response, 'CartilhaCae.pdf')

    def test_upload_file(self):
        response = self.c.get('/upload_file/')
        self.assertEquals(200, response.status_code)
        self.assertTemplateUsed(response, 'base_docs.html')
        self.assertTemplateUsed(response, 'upload_file.html')

    def test_viewpdf(self):
        response = self.c.get('/viewpdf/CartilhaCae.pdf', follow=True)
        self.assertEquals(200, response.status_code)
