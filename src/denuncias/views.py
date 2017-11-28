from django.shortcuts import render
# from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
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
        email_from = 'fiscaeinfo@gmail.com'
        email_to = ['fiscaeinfo@gmail.com']

        # msg = MIMEMultipart('alternative')

        text_school = 'Segue abaixo uma denuncia sobre a escola ' + school
        text_city = ' da cidade ' + city
        text_state = ' do estado ' + state
        text_end = ' situado no endereco ' + end + '\n\n'

        body = text_school + text_city + text_state + text_end + description

        msg = MIMEText(body.encode('utf-8'), 'text', 'utf-8')

        msg['From'] = email_from
        msg['To'] = email_to
        msg['Subject'] = Header(subject, 'utf-8')

        # text_school = 'Segue abaixo uma denuncia sobre a escola ' + school
        # text_city = 'da cidade ' + city
        # text_state = 'do estado ' + state
        # text_end = 'situado no endereco ' + end

        # messange = '\r\n'.join([
        #            'From: fiscaeinfo@gmail.com',
        #            'To: %s' % email_to,
        #            'Subject: %s' % subject,
        #            '',
        #            '%s' % text_school,
        #            '%s' % text_city,
        #            '%s' % text_state,
        #            '%s' % text_end,
        #            '%s' % description
        #            ])

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(email_from, 'fiscae2017')
        smtp.sendmail(email_from, email_to, msg.as_string())
        smtp.quit()

        return render(request, 'index.html')
    else:
        return render(request, 'denuncias/denunciations.html')
