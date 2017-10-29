from django.db import models
import json


class Question(models.Model):
    item_number = models.CharField(max_length=4, null=False)
    description = models.CharField(max_length=255, null=False)

    QUESTION_TYPE = (
        ('TA', 'Questões técnicas e administrativas'),
        ('HS', 'Questões Higiênico Sanitárias'),
        ('O', 'Questões orçamentárias'),
    )

    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE,
        default=1,
    )

    @staticmethod
    def seedQuestions():
        path = 'checklist/static/assets/test_items_checklist.json'
        # path = 'checklist/static/assets/items_checklist.json'
        with open(path) as json_file:
            checklist = json.load(json_file)
            for item in checklist['items']:
                Question(item_number=item['item_number'],
                         description=item['description']).save()

    @staticmethod
    def listQuestionsMethod():
        return Question.objects.all()
