from django.db import models


class ScheduleVisit(models.Model):
    school = models.TextField()
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
    def update(self):
        self.status = True