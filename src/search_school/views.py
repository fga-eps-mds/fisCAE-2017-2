from django.shortcuts import render, HttpResponseRedirect, reverse

import requests
import json

from .forms import SchoolForm


def getItems(name, state):
    items = {}
    urlBase = 'http://mobile-aceite.tcu.gov.br:80/nossaEscolaRS/'
    rest = 'rest/escolas?'
    name = 'nome=' + name.replace(" ", "%20")
    state = '&uf=' + state
    quantity = '&quantidadeDeItens=7'
    url = urlBase + rest + name + state + quantity
    request = requests.get(url)
    items = json.loads(request.text)
    return items


def getFilteredItems(name, state):
    items = getItems(name, state)
    schoolList = []
    for dictionary in items:
        for (key, value) in dictionary.items():
            if key == 'nome':
                schoolList.append(value)
    return schoolList


gList = []


def getList():
    global gList
    return gList


def search(request):
    if request.user.is_authenticated:
        context = {}
        schoolList = []
        if request.method == 'POST':
            schoolName = request.POST.get('school', 'Nao encontrado!')
            if schoolName == '':
                context['schoolName'] = ''
            else:
                state = 'TO'
                schoolList = getFilteredItems(schoolName, state)
                global gList
                gList = schoolList
                if not schoolList:
                    context['schoolName'] = 'Não encontrado'
                else:
                    return HttpResponseRedirect(
                            reverse('search_school:schoolForm')
                            )

        return render(
                    request,
                    'search.html',
                    {'schoolList': schoolList}
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
                                reverse('search_school:successSchool')
                                )
        else:
            schoolForm = SchoolForm(schools=gList)

        context = {'schoolForm': schoolForm}
        return render(request, 'schoolForm.html', context)

    else:
        return HttpResponseRedirect(reverse('search_school:notLoggedIn'))


def successSchool(request):
    return render(request, 'schoolSuccess.html')


def notLoggedIn(request):
    return render(request, 'notLoggedIn.html')
