from django.db import models
from django.apps import apps


class ScheduleVisit(models.Model):
    schoolName = models.TextField()
    schoolCode = models.TextField()
    date = models.TextField()
    time = models.TextField()
    members = models.TextField()
    status = models.BooleanField(default=False)
    nome_cae_schedule = models.CharField(max_length=50)

    @staticmethod
    def scheduleVisit(request):
        visits = []
        visits = ScheduleVisit.objects.all()
        return visits

    @staticmethod
    def updateStatus(self):
        Checklist = apps.get_model('checklist', 'Checklist')
        listChecklist = Checklist.objects.filter(visit_id=self.id)
        if len(listChecklist) == len(Checklist.CHECKLIST_TYPE):
            ScheduleVisit.objects.filter(pk=self.id).update(status=True)
