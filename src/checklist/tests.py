from django.test import TestCase, Client
from django.shortcuts import reverse

from .models import Question

from django.contrib.auth.models import User


class ChecklistTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="amanda", password="123")
        question = Question(
                        id=1,
                        item_number=1,
                        description="Agua parada",
                        question_type='TA'
                        )
        question.save()

    def testSubmitChecklistFormValid(self):
        client = Client()
        client.login(username="amanda", password="123")
        data = {'checklist_type': 'TA'}
        response = client.post(
                        reverse('checklist:checklistForm'),
                        data, follow=True
                        )
        print(response.redirect_chain)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.redirect_chain, [('/answerForm', 302)])

    def testSubmitChecklistFormInvalid(self):
        client = Client()
        client.login(username="amanda", password="123")
        data = {'checklist_type': 'TT'}
        response = client.post(
                        reverse('checklist:checklistForm'),
                        data,
                        follow=True
                        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.redirect_chain, [])

    def testRenderChecklistForm(self):
        client = Client()
        client.login(username="amanda", password="123")
        response = client.get(reverse('checklist:checklistForm'))
        self.assertEquals(response.status_code, 200)


class QuestionTeste(TestCase):
    def testSeed(self):
        Question.objects.all().delete()
        Question.seedQuestions()
        self.assertEquals(Question.objects.count(), 13)
