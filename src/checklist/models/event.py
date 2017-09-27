from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        abstract = True
