from django.db import models
from .school import School


class Checklist(models.Model):
    school = models.ForeignKey(School, related_name="checklists")

    def seedQuestions(self):
        pass

    def getQuestions(self):
        pass

    def validadeQuestion(self):
        pass
        
    @staticmethod
    def readQuestion():
        lista = []
        arq = open("checklist/questions.txt", "r")
        lista = arq.readlines()
        # lê linha por linha saltando 1
        # for linha in arq:
        # question = arq.readline()
        # lista.append(question)
        arq.close()
        return lista
