from django.shortcuts import render, HttpResponseRedirect, reverse
import json
import requests
from .forms import SchoolForm
from user.models import Advisor


gList = []
gSelectedSchool = {}


def getItems(name, state, city):
    items = {}
    urlBase = 'http://mobile-aceite.tcu.gov.br:80/nossaEscolaRS/'
    rest = 'rest/escolas?'
    name = 'nome=' + name.replace(" ", "%20")
    state = '&uf=' + state
    city = '&municipio=' + city
    quantity = '&quantidadeDeItens=7'
    category = '&rede=Publica'
    url = urlBase + rest + name + category + state + city + quantity
    request = requests.get(url)

    items = json.loads(request.text)
    return items


def getFilteredItems(name, state, city):
    items = getItems(name, state, city)
    schools = []
    for dictionary in items:
        school = {
            'nome':      dictionary.get('nome'),
            'codEscola': dictionary.get('codEscola'),
        }
        schools.append(school)

    return schools


def search(request):
    error = []
    global gList
    if request.user.is_authenticated:
        schools = []
        if request.method == 'POST':
            schoolName = request.POST.get('school', '')
            if schoolName.isspace():
                error = ['Preencha o nome.']
            else:
                current_user = request.user
                userId = current_user.id
                userObject = Advisor.objects.get(id=userId)
                state = (userObject.uf).upper()
                city = userObject.municipio
                schools = getFilteredItems(schoolName, state, city)
                gList = schools
                if not schools:
                    error = ['Não encontrado. Digite novamente']
                else:
                    return HttpResponseRedirect(
                        reverse('search_school:schoolForm')
                    )
        return render(
            request,
            'search.html',
            {'error': error}
        )
    else:
        return HttpResponseRedirect(reverse('notLoggedIn'))


def getSchoolNames(schoolList):
    schools = []
    for dictionary in schoolList:
        school = dictionary.get('nome')
        schools.append(school)
    return schools


def getSchoolDetail(list, name):
    for dictionary in list:
        for (key, value) in dictionary.items():
            value = dictionary.get('nome')
            if value == name:
                school = dictionary
    return school


def schoolForm(request):
    global gList
    global gSelectedSchool
    if request.user.is_authenticated:
        schools = getSchoolNames(gList)
        if request.method == 'POST':
            schoolForm = SchoolForm(request.POST, schools=schools)
            if schoolForm.is_valid():
                selectedSchool = request.POST.get('school')
                gSelectedSchool = getSchoolDetail(gList, selectedSchool)
                return HttpResponseRedirect(
                    reverse('agendar_visita:indexScheduleVisit')
                )
        else:
            schoolForm = SchoolForm(schools=schools)

        context = {'schoolForm': schoolForm}
        return render(request, 'schoolForm.html', context)

    else:
        return HttpResponseRedirect(reverse('notLoggedIn'))


def getSelectedSchool():
    global gSelectedSchool
    return gSelectedSchool
