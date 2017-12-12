from django.db import models
from .checklist import Checklist


class Observations(models.Model):
    observation = models.TextField()
    images = models.FileField()
    checklist = models.ForeignKey(
        Checklist,
        related_name="Observation",
        on_delete=models.CASCADE
    )
