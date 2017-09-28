from django.db import models
import json


class Question(models.Model):
    item_number = models.CharField(max_length=4, null=False)
    description = models.CharField(max_length=255, null=False)

    @staticmethod
    def seedQuestions():

        with open('checklist/static/assets/items_checklist.json') as json_file:
            checklist = json.load(json_file)
            for item in checklist['items']:
                Question(item_number=item['item_number'],
                         description=item['description']).save()

    @staticmethod
    def listQuestionsMethod():
        return Question.objects.all()
