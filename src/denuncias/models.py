from django.db import models

class Denunciation(models.Model):
    user_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField()