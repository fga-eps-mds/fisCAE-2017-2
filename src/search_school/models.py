from django.db import models


class School(models.Model):
    idSchool = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
