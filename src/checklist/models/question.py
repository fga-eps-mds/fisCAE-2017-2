from django.db import models


class Question(models.Model):
    description = models.CharField(max_length=255, null=False)
