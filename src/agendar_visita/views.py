from django.shortcuts import render, HttpResponseRedirect, reverse
from agendar_visita.models import ScheduleVisit
from search_school.views import getSelectedSchool
from user.models import Advisor
from .forms import VisitForm


def indexScheduleVisit(request):
    newSchedule = ScheduleVisit()
    school = getSelectedSchool
    if request.method == 'POST':
        newSchedule.school = getSelectedSchool()
        newSchedule.nome_cae_schedule = getNomeCaeSchedule() # nome do conselheiro que agendou a visita
        newSchedule.date = request.POST['date']
        newSchedule.time = request.POST['time']
        newSchedule.members = request.POST['members']
        newSchedule.save()
        return HttpResponseRedirect(
                            reverse('checklist:visitsSchool')
                            )
    return render(
                request,
                'indexScheduleVisit.html',
                {'school': school}
                )


def visitedScheduleds(request):
    current_user = request.user
    userId = current_user.id
    userObject = Advisor.objects.get(id=userId)
    nome_cae_user = userObject.nome_cae
    visited = ScheduleVisit.objects.filter(status=True,
                                           nome_cae_schedule=nome_cae_user)
    return render(
            request,
            'visitedScheduleds.html',
            {'visited': visited},
            )


def visitScheduled(request):
    current_user = request.user
    userId = current_user.id
    userObject = Advisor.objects.get(id=userId)
    nome_cae_user = userObject.nome_cae
    visits = ScheduleVisit.objects.filter(status=False,
                                          nome_cae_schedule=nome_cae_user)
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


def getNomeCaeSchedule(self):
    nome_cae_schedule = self.nome_cae_schedule
    return nome_cae_schedule
