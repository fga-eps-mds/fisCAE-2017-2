from django.db import models
from .school import School


class Checklist(models.Model):
    schools = models.ManyToManyField(School)  # ManyToMany em apenas um modelo
    questionList = models.TextField()

    def seedQuestions(self):
        pass

    def getQuestions(self):
        pass

    def validadeQuestion(self):
        pass
