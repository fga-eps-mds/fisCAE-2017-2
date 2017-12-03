from django.db import models


class Observations(models.Model):
    observation = models.TextField()
    images = models.FileField()
