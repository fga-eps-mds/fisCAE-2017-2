from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


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
