from django.db import models
from .checklist import Checklist
from .question import Question


class Answer(models.Model):

    answer = models.CharField(max_length=255, null=False)
    checklist = models.ForeignKey(Checklist, related_name="answers", on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
