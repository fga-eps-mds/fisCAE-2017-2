from django.test import TestCase, Client
from django.shortcuts import reverse
from agendar_visita.models import ScheduleVisit

from .models import Question

from django.contrib.auth.models import User


class ChecklistTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="amanda", password="123")
        question = Question(
            id=1,
            item_number=1,
            description="Agua parada",
            question_type='HS'
        )
        question.save()

        visit = ScheduleVisit(
            1, 'Escola Teste', '2017-10-10', '10:10', 'CAE', 0)
        visit.save()

    def testSubmitChecklistFormValid(self):
        client = Client()
        client.login(username="amanda", password="123")
        data = {'checklist_type': 'HS'}
        response = client.post(
            reverse('checklist:checklistForm', args=(1,)),
            data, follow=True
        )
        print(response.redirect_chain)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.redirect_chain, [('/responder/1/', 302)])

    def testSubmitChecklistFormInvalid(self):
        client = Client()
        client.login(username="amanda", password="123")
        data = {'checklist_type': 'TT'}
        response = client.post(
            reverse('checklist:checklistForm', args=(1,)),
            data,
            follow=True
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.redirect_chain, [])

    def testRenderChecklistForm(self):
        client = Client()
        client.login(username="amanda", password="123")
        response = client.get(reverse('checklist:checklistForm', args=(1,)))
        self.assertEquals(response.status_code, 200)

    def test_listSchools(self):
        c = Client()
        c.login(username="amanda", password="123")
        response = c.get('/lista-checklists/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listSchools.html')


class QuestionTeste(TestCase):
    def testSeed(self):
        Question.objects.all().delete()
        Question.seedQuestions()
        self.assertEquals(Question.objects.count(), 65)
