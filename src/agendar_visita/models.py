from django.db import models


class ScheduleVisit(models.Model):
    school = models.TextField()
    date = models.TextField()
    time = models.TextField()
    members = models.TextField()

    @staticmethod
    def scheduleVisit(request):
        visits = []
        visits = ScheduleVisit.objects.all()
        return visits
