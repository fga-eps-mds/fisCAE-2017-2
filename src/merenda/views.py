from django.shortcuts import render, get_object_or_404, redirect
from checklist.models.checklist import Checklist
from checklist.models import School
from checklist.models.question import Question
from checklist.models.answer import Answer
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse , HttpResponseRedirect
from acessar_documento.forms import UploadFileForm
from acessar_documento.models import Arquivos
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
import os.path
from django.core.files.storage import FileSystemStorage





def viewpdf(request):
    fs = FileSystemStorage()
    with fs.open('CartilhaCAE.pdf') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=CartilhaCAE.pdf'
        return response
    pdf.close()


def upload_file(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        arq = form.save(commit=False)
        arq.arquivo = request.FILES['arquivo']
        arq.save()
        # return render(request, 'documentsAll.html')
    return render(request, 'upload_file.html', {'form':form})


def documentsAll(request):
    lista = Arquivos.arquivosSalvos()
    return render(request,'documentsAll.html',{'lista':lista})



def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def findSchool(request):
    listSchool = School()
    listSchool = listSchool.searchSchool()
    foundSchool = ''
    try:
        if request.method == 'POST':
            schoolName = request.POST.get('school', 'Nao encontrado!!')
            # foundSchool = School.searchSchool(schoolName)
            for l in listSchool:
                if l.name == schoolName:
                    foundSchool = schoolName
                    return render(request, 'formSelect.html')
        return render(
            request,
            'findSchool.html',
            {'foundSchool': foundSchool, 'schoolName': schoolName}
        )
    except:
        return render(
            request,
            'findSchool.html',
            {'erro': 'Escola nao encontrada!!'}
        )

    # school = School(request.POST)
    # escola = School.searchSchool(school)
    # return render(request, 'findSchool.html', {'escola': escola})


def formSelect(request):
    return render(request, 'formSelect.html')


def check(request):
    html = ''
    newQuestion = Checklist()
    lista = newQuestion.readQuestion()
    for question in lista:
        html += '<a>' + question + '</a><br>'
    return render(request, 'check.html', {'questionList': lista})


def viewChecklist(request):
    schools = School.objects.all()
    answers = Answer.objects.filter(checklist_id=1)
    questions = Question.objects.all()
    return render(
        request,
        'viewchecklist.html',
        {'answers': answers, 'questions': questions, 'schools': schools}
    )


def tecForm(request):
    listQuestions = Question.listQuestionsMethod()
    return render(request, 'tecForm.html', {'listQuestions': listQuestions})


def access_doc(request):
    return render(request, 'access_doc.html')


def view_pdf_cae(request):
    return render(request, 'view_pdf_cae.html')


def Success(request):
    return render(request, 'Success.html')
