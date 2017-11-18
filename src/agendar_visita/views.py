from django.shortcuts import render, HttpResponseRedirect, reverse
from agendar_visita.models import ScheduleVisit
from search_school.views import getSelectedSchool
from .forms import VisitForm


def indexScheduleVisit(request):
    newSchedule = ScheduleVisit()
    schoolName = getSelectedSchool().get('nome')
    if request.method == 'POST':
        newSchedule.schoolName = schoolName
        newSchedule.schoolCode = getSelectedSchool().get('codEscola')
        newSchedule.date = request.POST['date']
        newSchedule.time = request.POST['time']
        newSchedule.members = request.POST['members']
        newSchedule.save()
        return HttpResponseRedirect(
                            reverse('agendar_visita:visitScheduled')
                            )
    return render(
                request,
                'indexScheduleVisit.html',
                {'school': schoolName}
                )


def visited(request):
    visited = ScheduleVisit.objects.filter(status=True)
    return render(
            request,
            'visitedScheduleds.html',
            {'visited': visited},
            )


def sceduled(request):
    visits = ScheduleVisit.objects.filter(status=False)
    return render(
            request,
            'visitScheduleds.html',
            {'visits': visits},
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
