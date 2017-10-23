from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def access_doc(request):
    return render(request, 'access_doc.html')


def view_pdf_cae(request):
    return render(request, 'view_pdf_cae.html')


def notLoggedIn(request):
    return render(request, 'notLoggedIn.html')
