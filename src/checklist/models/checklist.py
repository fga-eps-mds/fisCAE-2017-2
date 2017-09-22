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
    
    @staticmethod
    def readQuestion():
        lista = []
        arq = open("checklist/questions.txt","r")
        lista = arq.readlines()
        # lê linha por linha saltando 1
        # for linha in arq:
        # question = arq.readline()
        # lista.append(question)
        arq.close()    
        return lista