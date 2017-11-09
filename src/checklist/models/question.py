from django.db import models
import json


class Question(models.Model):
    item_number = models.CharField(max_length=4, null=False)
    description = models.CharField(max_length=255, null=False)

    QUESTION_TYPE = (
        ('TA', 'Questões técnicas e administrativas'),
        ('HS', 'Questões Higiênico Sanitárias'),
        ('AL', 'Questões Alimentares'),
        ('D', 'Sobre a documentação'),
    )

    question_type = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE,
        default=1,
    )

    @staticmethod
    def seedQuestions():
        path = 'static/assets/checklist_questions.json'
        # path = 'static/assets/test_items_checklist.json'
        # path = 'static/assets/items_checklist.json'
        with open(path) as json_file:
            checklist = json.load(json_file)
            for item in checklist['items']:
                Question(
                    item_number=item['item_number'],
                    description=item['description'],
                    question_type=item['question_type']).save()

    @staticmethod
    def listQuestionsMethod():
        return Question.objects.all()
