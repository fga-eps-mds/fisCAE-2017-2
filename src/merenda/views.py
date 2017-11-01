from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponseRedirect, reverse
from django.utils import timezone
from checklist.models.checklist import Checklist
from checklist.models.question import Question
from checklist.models.answer import Answer
from checklist.models.school import School
from user.models import User
from checklist.forms import ChecklistForm, AnswerForm
from agendar_reuniao.models import Agendamento
from agendar_reuniao.forms import AgendamentoForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render_to_response
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from acessar_documento.forms import UploadFileForm
from acessar_documento.models import Arquivos
from django.contrib.auth import authenticate, login, logout
import os.path
from django.contrib.auth.decorators import login_required
from user.forms import AdvisorForm
from user.models import Advisor



@login_required
def userEdit(request, pk):
    user = get_object_or_404(Advisor, pk=pk)
    form = AdvisorForm(request.POST or None, instance=user)
    if request.method == 'POST':
        form.save()
        return redirect('../../')
    return render(request, 'userEdit.html', {'form':form})

def edit_schedule(request, pk):
    reuniao = Agendamento.objects.get(id=pk)
    form = AgendamentoForm(request.POST or None, instance=reuniao)
    if form.is_valid():
        form.save()
        return redirect('../../scheduled.html')
    return render(request, 'edit_schedule.html', {'form': form})


def schedule_delete(request, pk):
    # reuniao = Agendamento.objects.get(pk=pk)
    Agendamento.objects.filter(id=pk).delete()
    return render(request, 'schedule_delete.html')


def indexScheduleMeeting(request):
    novoAgendamento = Agendamento()
    if request.method == 'POST':
        novoAgendamento.local = request.POST['local']
        novoAgendamento.data = request.POST['date']
        novoAgendamento.horario = request.POST['time']
        novoAgendamento.observacoes = request.POST['note']
        novoAgendamento.save()
    return render(request, 'indexScheduleMeeting.html')


def scheduled(request):
    todosAgendamentos = Agendamento.agendamentos(request)
    return render(request, 'scheduled.html',
                  {'todosAgendamentos': todosAgendamentos})


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


def getQuestions(checklist_type):
    questions = Question.objects.filter(question_type=checklist_type)
    return questions


questions = []


def answerForm(request):
    checklist = Checklist.objects.last()
    global questions

    if not questions:
        query_questions = Question.objects.filter(
            question_type=checklist.checklist_type
        )
        questions = list(query_questions)

    current_question = questions[0]

    if request.method == 'POST':
        answerForm = AnswerForm(request.POST)
        if answerForm.is_valid():
            answer = answerForm.save(commit=False)
            answer.checklist_id = checklist.id
            answer.question_id = current_question.id
            answer.save()
            questions.pop(0)
            if not questions:
                return HttpResponseRedirect(reverse('Success'))
            else:
                current_question = questions[0]
    else:
        answerForm = AnswerForm()
    return render(
        request,
        'answerForm.html',
        {
            'answerForm': answerForm,
            'current_question': current_question
        }
    )


def checklistForm(request):
    school = School(
        idSchool=111,
        name='EscolaTeste',
        state='DF',
        county='Brasília',
        address='Endereço',
        phone=111111,
        principal='Diretor'
    )
    school.save()
    if request.method == 'POST':
        checklistForm = ChecklistForm(request.POST)
        if checklistForm.is_valid():
            checklist = checklistForm.save(commit=False)
            checklist.user = request.user
            checklist.school = school
            checklist.created_date = timezone.now()
            checklist.save()
            return HttpResponseRedirect(
                reverse('answerForm')
            )
    else:
        checklistForm = ChecklistForm()
    return render(
        request,
        'checklistForm.html',
        {'checklistForm': checklistForm}
    )
