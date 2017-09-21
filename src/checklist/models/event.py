from django.db import models


class Event(models.Model):  # Abstrata, não será um modelo armazenado
    title = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        abstract = True
