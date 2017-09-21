from django.db import models
from .checklist import Checklist


class Question(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)

    QUESTIONS_TYPE = (
        ('O', 'Objetivas'),
        ('D', 'Discursivas')
    )
    questionType = models.TextField(
        choices=QUESTIONS_TYPE,
        default='Objetivas')
    description = models.TextField()
