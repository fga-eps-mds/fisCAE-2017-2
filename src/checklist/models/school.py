from django.db import models


class School(models.Model):
    idSchool = models.TextField()
    name = models.TextField()
    state = models.TextField()
    county = models.TextField()
    address = models.TextField()
    phone = models.TextField()
    principal = models.TextField()

    def searchSchool(request):
        # school = School.objects.get(name__contains=school)
        school = []
        school = School.objects.all()
        return school
