from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect, reverse
from django.utils import timezone
from checklist.models.checklist import Checklist
from checklist.models.question import Question
from checklist.models.answer import Answer
from checklist.models.school import School
from checklist.forms import ChecklistForm, AnswerForm
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from agendar_reuniao.models import Agendamento
from agendar_reuniao.forms import AgendamentoForm
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


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
    todosAgendamentos = Agendamento.agendamentos(request)
    return render(
            request,
            'scheduled.html',
            {'todosAgendamentos': todosAgendamentos}
            )


def schedules(request):
    return render(request, 'schedules.html')


def index(request):
    return render(request, 'index.html')


def access_doc(request):
    return render(request, 'access_doc.html')


def view_pdf_cae(request):
    fs = FileSystemStorage()
    with fs.open('static/assets/doc/CartilhaCAE.pdf') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=CartilhaCAE.pdf'
        return response
    pdf.close()


def notLoggedIn(request):
    return render(request, 'notLoggedIn.html')
