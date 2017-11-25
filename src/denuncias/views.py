from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Denunciation
import smtplib


def denunciations(request):
    if request.method == 'POST':
        denunciation = Denunciation()
        denunciation.email_from = request.POST['email']
        denunciation.subject = request.POST['subject']
        denunciation.password = request.POST['password']
        denunciation.description = request.POST['description']
#        denunciation.email_to = ['ouvidoria@fnde.gov.br', 'audit@fnde.gov.br']
        denunciation.email_to = ['mateusaugusto-2009@hotmail.com']

        email_from = denunciation.email_from
        email_to = denunciation.email_to
        subject = denunciation.subject
        password = denunciation.password
        description = denunciation.description

        messange = '\r\n'.join([
                   'From: %s' % email_from,
                   'To: %s' % email_to,
                   'Subject: %s' % subject,
                   '',
                   '%s' % description
                   ])

        smtp = smtplib.SMTP(email_from, 465)
        smtp.starttls()
        smtp.login(email_from, password)
        smtp.sendmail(email_from, email_to, messange)
        smtp.quit()

        denunciation.save()
        return HttpResponseRedirect(reverse('denuncias:denunciations'))

    return render(request, 'denuncias/denunciations.html')
