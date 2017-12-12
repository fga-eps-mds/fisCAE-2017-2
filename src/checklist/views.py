from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from checklist.models.checklist import Checklist
from checklist.models.question import Question
from agendar_visita.models import ScheduleVisit
from checklist.models.answer import Answer
from checklist.forms import ChecklistForm
from checklist.forms import AnswerForm
from checklist.forms import ObservationsForm
from user.models import Advisor
from django.core.exceptions import ObjectDoesNotExist


def getQuestions(checklist_type):
    questions = Question.objects.filter(question_type=checklist_type)
    return questions


def visitsSchool(request):
    current_user = request.user
    userId = current_user.id
    userObject = Advisor.objects.get(id=userId)
    nome_cae_user = userObject.nome_cae
    visita = ScheduleVisit.objects.filter(status=False,
                                          nome_cae_schedule=nome_cae_user)
    return render(request, 'visitsSchool.html', {'visita': visita})


var_id = 0


def checklistForm(request, id_visit):
    global var_id
    var_id = id_visit
    visit = ScheduleVisit.objects.get(id=id_visit)

    if request.user.is_authenticated:
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
                except ObjectDoesNotExist:
                    checklist.user = request.user
                    checklist.visit = visit
                    checklist.created_date = timezone.now()
                    checklist.save()

                    checklist.setNumberQuestions(checklist)

                url = reverse(
                        'checklist:answerForm',
                        args=[checklist.id]
                    )
                return HttpResponseRedirect(
                    url
                )
        else:
            checklistForm = ChecklistForm()

        context = {'checklistForm': checklistForm}
        return render(request, 'checklistForm.html', context)

    else:
        return HttpResponseRedirect(reverse('notLoggedIn'))


def completed(request, checklist_id):
        checklist = Checklist.objects.get(
            id=checklist_id,
            )
        form = ObservationsForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.images = request.FILES['images']
            observation.observation = request.POST['observation']
            observation.checklist = checklist
            observation.save()
        # return render(request, 'documentsAll.html')
        return render(
               request, 'completed.html',
               {'var_id': var_id, 'form': form}
               )


def getQuestion(checklist):
    questionNumber = checklist.last_question + 1
    question = Question.objects.get(
                        id=questionNumber,
                        )

    return question


def answerForm(request, checklist_id):
    if request.user.is_authenticated:
        user = request.user
        checklist = Checklist.objects.get(
            id=checklist_id,
            user_id=user.id,
            )
        if checklist.status:
            return HttpResponseRedirect(
                   reverse('checklist:completed', args=[checklist.id])
                   )
        else:
            question = getQuestion(checklist)
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
                        return HttpResponseRedirect(reverse(
                                            'checklist:completed')
                                            )
                    else:
                        redirect_url = reverse(
                            'checklist:answerForm',
                            args=[checklist.id]
                        )
                        return HttpResponseRedirect(
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
    except ObjectDoesNotExist:
        context = {
            'error': 'checklist não encontrado'
        }

    return render(request, 'showAnswers.html', context)


def listSchools(request):
    visits = ScheduleVisit.objects.all()
    checklists = Checklist.objects.all()
    context = {
        'visits': visits,
        'checklists': checklists
    }

    return render(request, 'listSchools.html', context)
