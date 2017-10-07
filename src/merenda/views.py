from django.shortcuts import render
from checklist.models.checklist import Checklist
from checklist.models import School
from checklist.models.question import Question
from checklist.models.answer import Answer
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


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
    fs = FileSystemStorage()
    with fs.open('static/assets/doc/CartilhaCAE.pdf') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=CartilhaCAE.pdf'
        return response
    pdf.close()


def Success(request):
    return render(request, 'Success.html')
