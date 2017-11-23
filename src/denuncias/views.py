from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
import smtplib

from .models import Denunciation


def denunciations(request):
    if request.method == 'POST':
        denunciation = Denunciation()
        denunciation.user_name = request.POST['user_name']
        denunciation.email = request.POST['email']
        denunciation.description = request.POST['description']
        
        smtp = smtplib.SMTP('email@email.com', 999)
        smtp.starttls()

        smtp.login('fisCae@gmail.com', 'senha')

        de = 'fisCae@gmail.com'
        para = ['emailEnvio']
        assunto = 'Denúncia'
        msg = '\r\n'.join([
            'From: %s' % de,
            'To: %s' % para,
            'Subject: %s' % assunto,
            '',
            '%s' % denunciation.description
        ])

        smtp.sendmail(de, para, msg)
        smtp.quit()
        
        denunciation.save()
        return HttpResponseRedirect(reverse('denuncias:denunciations'))
    


    return render(request, 'denuncias/denunciations.html')

