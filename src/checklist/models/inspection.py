from django.db import models
from .event import Event


class Inspection(Event):
    author = models.CharField(max_length=50)
    pass
