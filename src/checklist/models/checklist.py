from django.db import models
from django.utils import timezone

from .school import School
from user.models import User


class Checklist(models.Model):
    school = models.ForeignKey(
        School,
        related_name="checklists",
        on_delete=models.CASCADE
    )

    # author = models.ForeignKey('auth.User')
    # user = models.OneToOneField(User)
    user = models.ForeignKey('auth.User')

    CHECKLIST_TYPE = (
        ('TA', 'Questões técnicas e administrativas'),
        ('HS', 'Questões Higiênico Sanitárias'),
        ('O', 'Questões orçamentárias'),
    )
    checklist_type = models.CharField(
        max_length=2,
        choices=CHECKLIST_TYPE,
        default=1,
    )

    created_date = models.DateTimeField(
            default=timezone.now)

    def getQuestions(self):
        pass

    def validaQuestion(self):
        pass

    """
    @staticmethod
    def readQuestion():
        lista = []
        arq = open("checklist/questions.txt", "r")
        lista = arq.readlines()
        # le linha por linha saltando 1
        # for linha in arq:
        # question = arq.readline()
        # lista.append(question)
        arq.close()
        return lista
    """
