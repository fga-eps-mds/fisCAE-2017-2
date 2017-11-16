from django.db import models


class Profile(models.Model):
    code = models.IntegerField(blank=False)
    description = models.CharField(max_length=255, blank=False)
