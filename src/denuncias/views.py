from django.shortcuts import render
import smtplib


def denunciations(request):
    if request.method == 'POST':
        school = request.POST['escola']
        city = request.POST['cidade']
        state = request.POST['estado']
        end = request.POST['endereco']
        subject = request.POST['subject']
        description = request.POST['description'] 
#       email_to = ['ouvidoria@fnde.gov.br', 'audit@fnde.gov.br']
        email_to = ['fiscaeinfo@gmail.com']

        text_school = 'Segue abaixo uma denuncia sobre a escola ' + school
        text_city = 'da cidade ' + city
        text_state = 'do estado ' + state
        text_end = 'situado no endereco ' + end

        messange = '\r\n'.join([
                   'From: fiscaeinfo@gmail.com',
                   'To: %s' % email_to,
                   'Subject: %s' % subject,
                   '',
                   '%s' % text_school,
                   '%s' % text_city,
                   '%s' % text_state,
                   '%s' % text_end,
                   '%s' % description
                   ])

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login('fiscaeinfo@gmail.com', 'fiscae2017')
        smtp.sendmail('fiscaeinfo@gmail.com', email_to, messange)
        smtp.quit()

        return render(request, 'index.html')
    else:
        return render(request, 'denuncias/denunciations.html')
