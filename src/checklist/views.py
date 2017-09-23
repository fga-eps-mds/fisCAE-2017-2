from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models.checklist import Checklist
from django.template import RequestContext
from django.template import Template


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def findSchool(request):
    return render(request, 'findSchool.html')


def formSelect(request):
    return render(request, 'formSelect.html')


def check(request):
    html = ''
    newQuestion = Checklist()
    lista = newQuestion.readQuestion()
    for question in lista:
        html += '<a>' + question + '</a><br>'
    return render(request, 'check.html', {'questionList': lista})
