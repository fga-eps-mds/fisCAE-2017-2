from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models.checklist import Checklist


def index(request):
	html = ''
	newQuestion = Checklist()
	lista = newQuestion.readQuestion()
	for question in lista:
		html += '<a>' + question + '</a><br>'
	# return HttpResponse(html)
	return render(request ,'index.html')

