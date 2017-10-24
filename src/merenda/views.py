from django.shortcuts import render
from agendar_reuniao.models import Agendamento
from django.shortcuts import redirect
from agendar_reuniao.forms import AgendamentoForm


def edit_schedule(request, pk):
    reuniao = Agendamento.objects.get(id=pk)
    form = AgendamentoForm(request.POST or None, instance=reuniao)
    if form.is_valid():
        form.save()
        return redirect('../../scheduled.html')
    return render(request, 'edit_schedule.html', {'form': form})


def schedule_delete(request, pk):
    # reuniao = Agendamento.objects.get(pk=pk)
    Agendamento.objects.filter(id=pk).delete()
    return render(request, 'schedule_delete.html')


def indexScheduleMeeting(request):
    novoAgendamento = Agendamento()
    if request.method == 'POST':
        novoAgendamento.local = request.POST['local']
        novoAgendamento.data = request.POST['date']
        novoAgendamento.horario = request.POST['time']
        novoAgendamento.observacoes = request.POST['note']
        novoAgendamento.save()
    return render(request, 'indexScheduleMeeting.html')


def scheduled(request):
    todosAgendamentos = Agendamento.agendamentos(request)
    return render(
            request,
            'scheduled.html',
            {'todosAgendamentos': todosAgendamentos}
            )


def index(request):
    return render(request, 'index.html')


def access_doc(request):
    return render(request, 'access_doc.html')


def view_pdf_cae(request):
    return render(request, 'view_pdf_cae.html')


def notLoggedIn(request):
    return render(request, 'notLoggedIn.html')


def Success(request):
    return render(request, 'Success.html')