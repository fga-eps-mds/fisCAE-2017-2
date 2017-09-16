from django.db import models

# Create your models here.
class advisor(models.Model):
    name=models.CharField(max_lenght=64, null=False)
    phone=models.CharField(max_lenght=13,null=True)
    email=models.CharField(max_lenght=100,null=True)
    cpf=models.CharField(max_lenght=14,null=False)
    #endereço
    cep=models.CharField(max_lenght=10,null=False)
    descricao=models.CharField(max_lenght=50,null=True)
    bairro=models.CharField(max_lenght=30,null=False)
    municipio=models.CharField(max_lenght=30,null=False)
    uf=models.CharField(max_lenght=2,null=False)
    #endereço
    
