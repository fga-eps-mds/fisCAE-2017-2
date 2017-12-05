from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=100, null=False)


class Advisor(Person):
    cpf = models.CharField(max_length=14, null=False)
    tipo_cae = models.CharField(default='Municipal', max_length=9, null=False)
    nome_cae = models.CharField(default='CAE', max_length=50, null=False)
    cep = models.CharField(max_length=10, null=False)
    bairro = models.CharField(max_length=30, null=False)
    municipio = models.CharField(max_length=30, null=False)
    uf = models.CharField(max_length=2, null=False)

    class Meta:
        permissions = (
            ('fill_checklist', 'Advisor can fill out checklist'),
        )


class President(Advisor):
    class Meta:
        permissions = (
            ('president', 'President permissions'),
        )


class Administrator(Person):
    class Meta:
        permissions = (
            ('administrator', 'Administrator permissions'),
        )
