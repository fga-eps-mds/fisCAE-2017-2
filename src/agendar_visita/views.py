from django.shortcuts import render, HttpResponseRedirect, reverse
from agendar_visita.models import ScheduleVisit
from search_school.views import getSelectedSchool
from .forms import VisitForm


def indexScheduleVisit(request):
    newSchedule = ScheduleVisit()
    if request.method == 'POST':
        newSchedule.school = getSelectedSchool()
        newSchedule.date = request.POST['date']
        newSchedule.time = request.POST['time']
        newSchedule.members = request.POST['members']
        newSchedule.save()
        return HttpResponseRedirect(
                            reverse('agendar_visita:visitScheduled')
                            )
    return render(request, 'indexScheduleVisit.html')


def visitScheduled(request):
    allSchedules = ScheduleVisit.scheduleVisit(request)
    return render(
            request,
            'visitScheduleds.html',
            {'allSchedules': allSchedules}
            )


def scheduleVisitDelete(request, pk):
    ScheduleVisit.objects.filter(id=pk).delete()
    return render(request, 'deleteScheduleVisit.html')


def editVisit(request, pk):
    visit = ScheduleVisit.objects.get(id=pk)
    form = VisitForm(request.POST or None, instance=visit)
    school = visit.school
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(
                            reverse('agendar_visita:visitScheduled')
                            )
    return render(request, 'editVisit.html', {'form': form, 'school': school})
