from django.db import models


class ScheduleVisit(models.Model):
    school = models.TextField()
    date = models.TextField()
    time = models.TextField()
    members = models.TextField()
    status = models.BooleanField(default=False)

    @staticmethod
    def scheduleVisit(request):
        visits = []
        visits = ScheduleVisit.objects.all()
        return visits

    @staticmethod
    def update(self):
        self.status = True