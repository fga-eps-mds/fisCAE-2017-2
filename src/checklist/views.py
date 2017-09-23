from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models.checklist import Checklist
from  django.template import RequestContext
from django.template import Template


def index(request):
	return render(request, 'index.html')


def check(request):
	html = ''
	newQuestion = Checklist()
	lista = newQuestion.readQuestion()
	for question in lista:
		html += '<a>' + question + '</a><br>'
	return render(request, 'check.html', {'questionList': lista})




