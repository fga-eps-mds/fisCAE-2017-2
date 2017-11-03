
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect, reverse
from django.utils import timezone
from checklist.models.checklist import Checklist
from checklist.models.question import Question
from checklist.models.answer import Answer
from checklist.models.school import School
from checklist.forms import ChecklistForm, AnswerForm
from agendar_reuniao.models import Agendamento
from agendar_reuniao.forms import AgendamentoForm
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


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
    return render(
            request,
            'scheduled.html',
            {'todosAgendamentos': todosAgendamentos}
            )


def index(request):
    return render(request, 'index.html')


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
    return render(request, 'view_pdf_cae.html')


def notLoggedIn(request):
    return render(request, 'notLoggedIn.html')

