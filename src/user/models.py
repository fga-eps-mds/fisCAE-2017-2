from django.db import models


class advisor(models.Model):
    name = models.CharField(max_length=64, null=False)
    phone = models.CharField(max_length=13, null=True)
    email = models.CharField(max_length=100, null=True)
    cpf = models.CharField(max_length=14, null=False)
    # endereço
    cep = models.CharField(max_length=10, null=False)
    descricao = models.CharField(max_length=50, null=True)
    bairro = models.CharField(max_length=30, null=False)
    municipio = models.CharField(max_length=30, null=False)
    uf = models.CharField(max_length=2, null=False)
    # endereço
