from django.db import models


class Denunciation(models.Model):
    email_from = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    email_to = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField()
