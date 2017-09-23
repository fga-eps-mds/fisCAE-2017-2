from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def findSchool(request):
    return render(request, 'findSchool.html')
