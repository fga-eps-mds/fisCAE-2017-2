from django.db import models
from .question import Question
from .checklist import Checklist


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)

    ANSWER_TYPE = (
        ('O', 'Objetiva'),
        ('D', 'Discursiva')
    )

    answer = models.TextField()

    def __str__(self):
        return self.answer
