from django.db import models
from django.contrib.auth.models import User


class Advisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=False)
    email = models.EmailField(max_length=100, null=False)
    cpf = models.CharField(max_length=14, null=False)
    cep = models.CharField(max_length=10, null=False)
    bairro = models.CharField(max_length=30, null=False)
    municipio = models.CharField(max_length=30, null=False)
    uf = models.CharField(max_length=2, null=False)


class President(Advisor):
    class Meta:
        permissions = (
            ('add_advisor', 'President can add Advisor'),
            ('remove_advisor', 'President can remove Advisor'),
        )


class Administrator(Advisor):
    class Meta:
        permissions = (
            ('add_president', 'Administrator can add President'),
            ('remove_president', 'Administrator can remove President'),
        )