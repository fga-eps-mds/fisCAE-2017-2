from django.shortcuts import render
from email.mime.text import MIMEText
import smtplib


def sendmaildenunciation(request, texto, subject, emails):
    mensagem = MIMEText(texto)
    mensagem.set_charset('utf-8')
    mensagem['Subject'] = subject
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('noreplayfiscae@gmail.com', 'fiscaeunb')
    mail.sendmail('noreplayfiscae@gmail.com', emails, mensagem.as_string())


def denunciations(request):
    if request.method == 'POST':
        school = request.POST['escola']
        city = request.POST['cidade']
        state = request.POST['estado']
        end = request.POST['endereco']
        subject = request.POST['subject']
        description = request.POST['description']
        email_to = ['ouvidoria@fnde.gov.br', 'audit@fnde.gov.br']
        # email_to = ['noreplayfiscae@gmail.com']

        text_school = 'Segue abaixo uma denúncia sobre a escola ' + school
        text_city = ' da cidade ' + city
        text_state = ' do estado ' + state
        text_end = ' situado no endereço ' + end + ':\n\n'

        text = text_school + text_city + text_state + text_end + description

        sendmaildenunciation(request, text, subject, email_to)

        mensagem = 'Denúncia Enviada!'

        return render(request, 'denuncias/sucess_send_denunciation.html', {
            'mensagem': mensagem
        })
    else:
        return render(request, 'denuncias/denunciations.html')
