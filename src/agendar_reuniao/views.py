from django.shortcuts import render, HttpResponseRedirect, reverse
from agendar_reuniao.models import Agendamento
from agendar_reuniao.forms import AgendamentoForm
from user.models import Advisor
import smtplib
from django.contrib.auth.decorators import login_required
# from email.MIMEText import MIMEText
# from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendmailfunction(request, texto, todosemails):
    mensagem = MIMEText(texto)
    mensagem.set_charset('utf-8')
    mensagem['Subject'] = "Novo evento CAE"
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('noreplayfiscae@gmail.com', 'fiscaeunb')
    for i in todosemails:
        mail.sendmail('noreplayfiscae@gmail.com', i.email, mensagem.as_string())


def notify(request, novoAgendamento, tipo):
    current_user = request.user
    userId = current_user.id
    userObject = Advisor.objects.get(id=userId)
    cae_user = userObject.nome_cae
    user_name = userObject.name
    todosemails = Advisor.objects.filter(nome_cae=cae_user)
    texto = user_name + " membro do " + cae_user + " agendou uma " + tipo + ":"

    if tipo == "reunião":
        data = novoAgendamento.data
        local = novoAgendamento.local
        horario = novoAgendamento.horario
        observacoes = novoAgendamento.observacoes
        texto += '\n Data: ' + data + '\n Local: ' + local
        texto += '\n Horário: ' + horario + '\n Observações: ' + observacoes
    elif tipo == "visita":
        nome_cae = novoAgendamento.nome_cae_schedule
        schooolname = novoAgendamento.schoolName
        schoolcode = novoAgendamento.schoolCode
        data = novoAgendamento.date
        time = novoAgendamento.time
        texto += '\n Nome do Cae: ' + nome_cae
        texto += '\n Nome da escola: ' + schooolname
        texto += '\n Código da escola: ' + str(schoolcode) + '\n Data: ' + data
        texto += '\n Horário ' + time
    sendmailfunction(request, texto, todosemails)


@login_required
def edit_schedule(request, pk):
    reuniao = Agendamento.objects.get(id=pk)
    form = AgendamentoForm(request.POST or None, instance=reuniao)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('agendar_reuniao:scheduled'))
    return render(request, 'edit_schedule.html', {'form': form})


def schedule_delete(request, pk):
    Agendamento.objects.filter(id=pk).delete()
    return render(request, 'schedule_delete.html')


def indexScheduleMeeting(request):
    novoAgendamento = Agendamento()
    if request.method == 'POST':
        tipo = "reunião"
        current_user = request.user
        userId = current_user.id
        userObject = Advisor.objects.get(id=userId)
        novoAgendamento.nome_cae_schedule = userObject.nome_cae
        novoAgendamento.local = request.POST['local']
        novoAgendamento.data = request.POST['date']
        novoAgendamento.horario = request.POST['time']
        novoAgendamento.observacoes = request.POST['note']
        novoAgendamento.save()
        notify(request, novoAgendamento, tipo)
        return HttpResponseRedirect(reverse('agendar_reuniao:scheduled'))
    return render(request, 'indexScheduleMeeting.html')


def current(request):
    current_user = request.user
    userId = current_user.id
    userObject = Advisor.objects.get(id=userId)
    return (userObject)


def scheduled(request):
    try:
        userObject_scheduled = current(request)
        cae_user = userObject_scheduled.nome_cae
        todosAgendamentos = Agendamento.objects.filter(
            nome_cae_schedule=cae_user)

        return render(request, 'scheduled.html', {
            'todosAgendamentos': todosAgendamentos
        })
    except:

        mensagem1 = "Apenas membros de CAE podem "
        mensagem2 = "ter acesso à essas funcionalidades!"
        mensagem = mensagem1 + mensagem2
        return render(request, 'schedules.html', {'mensagem': mensagem})


def schedules(request):
    return render(request, 'schedules.html')
