from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone

from checklist.models.checklist import Checklist
from checklist.models.question import Question
from checklist.models.school import School
from agendar_visita.models import ScheduleVisit
from checklist.models.answer import Answer
from checklist.forms import ChecklistForm
from checklist.forms import AnswerForm


def getQuestions(checklist_type):
    questions = Question.objects.filter(question_type=checklist_type)
    return questions


def visitsSchool(request):
    visita = ScheduleVisit.objects.filter(status=False)
    return render(request, 'visitsSchool.html', {'visita': visita})


var_id = 0


def checklistForm(request, id_visit):
    global var_id
    var_id = id_visit
    visit = ScheduleVisit.objects.get(id=id_visit)

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
                try:
                    tempChecklist = Checklist.objects.get(
                        visit_id=id_visit,
                        checklist_type=checklist.checklist_type
                        )
                    checklist = tempChecklist
                except:
                    checklist.user = request.user
                    checklist.school = school
                    checklist.visit = visit
                    checklist.created_date = timezone.now()
                    checklist.save()

                    checklist.setNumberQuestions(checklist)

                listChecklist = Checklist.objects.filter(visit_id=id_visit)

                if len(listChecklist) == len(Checklist.CHECKLIST_TYPE):
                    visit.update(visit)

                redirect_url = reverse(
                    'checklist:answerForm',
                    args=[checklist.id]
                    )
                return HttpResponseRedirect(
                    redirect_url
                )
        else:
            checklistForm = ChecklistForm()

        context = {'checklistForm': checklistForm}
        return render(request, 'checklistForm.html', context)

    else:
        return HttpResponseRedirect(reverse('notLoggedIn'))


questions = []


def success(request):
    return render(request, 'success.html', {'var_id': var_id})


def completed(request):
    return render(request, 'completed.html', {'var_id': var_id})


def checkQuestions(checklist):
    global questions
    if not questions:
        query_questions = Question.objects.filter(
            question_type=checklist.checklist_type
        )
        questions = list(query_questions)


def answerForm(request, checklist_id):
    if request.user.is_authenticated:
        user = request.user
        checklist = Checklist.objects.get(
            id=checklist_id,
            user_id=user.id,
            )
        if checklist.status:
            return HttpResponseRedirect(reverse('checklist:completed'))
        else:
            questionNumber = checklist.last_question + 1
            question = Question.objects.get(
                        id=questionNumber,
                        )

            if request.method == 'POST':
                answerForm = AnswerForm(request.POST)
                if answerForm.is_valid():
                    answer = answerForm.save(commit=False)
                    answer.checklist_id = checklist.id
                    answer.question_id = question.id
                    answer.user = request.user
                    answer.save()

                    checklist.updateStatus(checklist, question.id)

                    answerForm = AnswerForm()
                    if checklist.status:
                        return HttpResponseRedirect(reverse('checklist:success'))
                    else:
                        redirect_url = reverse(
                            'checklist:answerForm',
                            args=[checklist.id]
                        )
                        return HttpResponseRedirect(
                            # reverse('checklist:answerForm')
                            redirect_url
                        )
            else:
                answerForm = AnswerForm()
            context = {
                'answerForm': answerForm,
                'current_question': question
            }
            return render(request, 'answerForm.html', context)
    else:
        return HttpResponseRedirect(reverse('notLoggedIn'))


def showAnswers(request, id):
    try:
        checklist = Checklist.objects.get(pk=id)
        answers = Answer.objects.filter(user=request.user, checklist=checklist)
        context = {
            'answers': answers
        }
    except:
        context = {
            'error': 'checklist não encontrado'
        }

    return render(request, 'showAnswers.html', context)


def listSchools(request):
    schools = School.objects.all()

    context = {
        'schools': schools
    }

    return render(request, 'listSchools.html', context)
