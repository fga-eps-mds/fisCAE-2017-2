from django.shortcuts import render
from checklist.models.checklist import Checklist
from checklist.models import School
from checklist.models.question import Question
from checklist.models.answer import Answer
from agendar_reuniao.models import Agendamento


def schedule_delete(request, pk):
    # reuniao = Agendamento.objects.get(pk=pk)
    Agendamento.objects.filter(id=pk).delete() 
    return render(request, 'schedule_delete.html')  


def indexScheduleMeeting(request):
    novoAgendamento = Agendamento()
    if request.method == 'POST':
        novoAgendamento.local = request.POST['local']
        # novoAgendamento.data = request.POST['date']
        # novoAgendamento.horario = request.POST['time']
        # novoAgendamento.observacoes = request.POST['note']
        novoAgendamento.save()
    return render(request, 'indexScheduleMeeting.html')


def scheduled(request):
    todosAgendamentos = Agendamento.agendamentos(request)
    return render(request, 'scheduled.html', {'todosAgendamentos': todosAgendamentos})


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