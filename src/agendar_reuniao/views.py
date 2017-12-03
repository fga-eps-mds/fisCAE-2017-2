from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from agendar_reuniao.models import Agendamento
from agendar_reuniao.forms import AgendamentoForm
from user.models import Advisor


def edit_schedule(request, pk):
    reuniao = Agendamento.objects.get(id=pk)
    form = AgendamentoForm(request.POST or None, instance=reuniao)
    if form.is_valid():
        form.save()
        return redirect('../../scheduled.html')
    return render(request, 'edit_schedule.html', {'form': form})


def schedule_delete(request, pk):
    Agendamento.objects.filter(id=pk).delete()
    return render(request, 'schedule_delete.html')


def indexScheduleMeeting(request):
    novoAgendamento = Agendamento()
    if request.method == 'POST':
        current_user = request.user
        userId = current_user.id
        userObject = Advisor.objects.get(id=userId)
        novoAgendamento.nome_cae_schedule = userObject.nome_cae
        novoAgendamento.local = request.POST['local']
        novoAgendamento.data = request.POST['date']
        novoAgendamento.horario = request.POST['time']
        novoAgendamento.observacoes = request.POST['note']
        novoAgendamento.save()
        return HttpResponseRedirect(
                            reverse('agendar_reuniao:scheduled')
                            )
    return render(request, 'indexScheduleMeeting.html')


def scheduled(request):
    current_user = request.user
    userId = current_user.id
    userObject = Advisor.objects.get(id=userId)
    cae_user = userObject.nome_cae
    todosAgendamentos = Agendamento.objects.filter(nome_cae_schedule=cae_user)
    return render(
            request,
            'scheduled.html',
            {'todosAgendamentos': todosAgendamentos}
            )


def schedules(request):
    return render(request, 'schedules.html')
