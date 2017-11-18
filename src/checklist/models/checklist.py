from django.db import models
from django.utils import timezone
from django.apps import apps
from agendar_visita.models import ScheduleVisit
from .question import Question


class Checklist(models.Model):
    visit = models.ForeignKey(
        ScheduleVisit,
        related_name="checklists",
        on_delete=models.CASCADE
    )

    user = models.ForeignKey('auth.User')

    CHECKLIST_TYPE = (
        ('TA', 'Questões técnicas e administrativas'),
        ('HS', 'Questões Higiênico Sanitárias'),
        ('O', 'Questões orçamentárias'),
    )
    checklist_type = models.CharField(
        max_length=2,
        choices=CHECKLIST_TYPE,
        default=None,
    )

    created_date = models.DateTimeField(
            default=timezone.now
            )

    number_questions = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    last_question = models.IntegerField(default=0)

    @staticmethod
    def countTypes(CHECKLIST_TYPE):
        return len(CHECKLIST_TYPE)

    @staticmethod
    def updateStatus(self, question_id):
        Answer = apps.get_model('checklist', 'Answer')
        answers = Answer.objects.filter(checklist_id=self.id)
        Checklist.objects.filter(pk=self.id).update(last_question=question_id)
        if len(answers) == self.number_questions:
            Checklist.objects.filter(pk=self.id).update(status=True)
            visit = ScheduleVisit.objects.get(id=self.visit_id)
            visit.updateStatus(visit)

    @staticmethod
    def setNumberQuestions(self):
        checklist_type = self.checklist_type
        questions = Question.objects.filter(question_type=checklist_type)
        Checklist.objects.filter(pk=self.id).update(
            last_question=questions[0].id - 1
            )
        Checklist.objects.filter(pk=self.id).update(
            number_questions=len(questions)
            )
