from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def notLoggedIn(request):
    return render(request, 'notLoggedIn.html')


def about(request):
    return render(request, 'about.html')
