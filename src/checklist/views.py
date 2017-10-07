from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone

from checklist.models.checklist import Checklist
from checklist.models.question import Question
from checklist.models.school import School

from checklist.forms import ChecklistForm
from checklist.forms import AnswerForm


def success(request):
    return render(request, 'success.html')


def notLoggedIn(request):
    return render(request, 'notLoggedIn.html')


def getQuestions(checklist_type):
    questions = Question.objects.filter(question_type=checklist_type)
    return questions


questions = []


def answerForm(request):
    if request.user.is_authenticated:
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
                    return HttpResponseRedirect(reverse('checklist:success'))
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
    else:
        return HttpResponseRedirect(reverse('notLoggedIn'))


def checklistForm(request):
    if request.user.is_authenticated:
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
                            reverse('checklist:answerForm')
                            )
        else:
            checklistForm = ChecklistForm()
        return render(
                    request,
                    'checklistForm.html',
                    {'checklistForm': checklistForm}
                )
    else:
        return HttpResponseRedirect(reverse('notLoggedIn'))
