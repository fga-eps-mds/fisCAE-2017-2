from django.shortcuts import render, HttpResponseRedirect, reverse
import requests
import json
from .forms import SchoolForm
from user.models import Advisor


def getItems(name, state, city):
    items = {}
    urlBase = 'http://mobile-aceite.tcu.gov.br:80/nossaEscolaRS/'
    rest = 'rest/escolas?'
    name = 'nome=' + name.replace(" ", "%20")
    state = '&uf=' + state
    city = '&municipio=' + city
    quantity = '&quantidadeDeItens=7'
    url = urlBase + rest + name + state + city + quantity
    request = requests.get(url)
    items = json.loads(request.text)
    return items


def getFilteredItems(name, state, city):
    items = getItems(name, state, city)
    schoolList = []
    for dictionary in items:
        for (key, value) in dictionary.items():
            if key == 'nome':
                schoolList.append(value)
    return schoolList


gList = []


def search(request):
    error = []
    if request.user.is_authenticated:
        schoolList = []
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
                print((userObject.uf).upper(), city)
                schoolList = getFilteredItems(schoolName, state, city)
                global gList
                gList = schoolList
                if not schoolList:
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
        return HttpResponseRedirect(reverse('search_school:notLoggedIn'))


def schoolForm(request):
    global gList
    if request.user.is_authenticated:
        if request.method == 'POST':
            schoolForm = SchoolForm(request.POST, schools=gList)
            if schoolForm.is_valid():
                selectedSchool = request.POST.get('school')
                print(selectedSchool)
                return HttpResponseRedirect(
                    reverse('search_school:redirectSchool')
                )
        else:
            schoolForm = SchoolForm(schools=gList)

        context = {'schoolForm': schoolForm}
        return render(request, 'schoolForm.html', context)

    else:
        return HttpResponseRedirect(reverse('search_school:notLoggedIn'))


def redirectSchool(request):
    return render(request, 'redirectSchool.html')


def notLoggedIn(request):
    return render(request, 'notLoggedIn.html')
