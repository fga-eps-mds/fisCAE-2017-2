from django.db import models
from .checklist import Checklist
from .question import Question
from django.contrib.auth.models import User


class Answer(models.Model):
    checklist = models.ForeignKey(
        Checklist,
        related_name="answers",
        on_delete=models.CASCADE
    )
    question = models.ForeignKey(
        Question,
        related_name="answers",
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    ANSWER_CHOICE = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    answer = models.CharField(
        max_length=2,
        choices=ANSWER_CHOICE,
        default=None,
    )
