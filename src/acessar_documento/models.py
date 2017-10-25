from django.db import models
from django.forms import ModelForm

class Arquivos(models.Model):
    title = models.TextField()
    arquivo = models.FileField(upload_to='../uploads')
    @staticmethod
    def arquivosSalvos():
        lista = ''
        lista = Arquivos.objects.all()
        return lista
