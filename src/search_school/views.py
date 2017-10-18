from django.shortcuts import render, HttpResponseRedirect, reverse

import requests
import json


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
            # apply filter
            if key == 'nome':
                schoolList.append(value)
    return schoolList


def search(request):
    if request.user.is_authenticated:
        context = {}
        schoolList = []
        if request.method == 'POST':
            schoolName = request.POST.get('school', 'Nao encontrado!')
            if schoolName == '':
                context['schoolName'] = ''
            else:
                state = 'RO'
                schoolList = getFilteredItems(schoolName, state)
                if not schoolList:
                    context['schoolName'] = 'Não encontrado'
                else:
                    pass

        return render(
                    request,
                    'search.html',
                    {'schoolList': schoolList}
                )
    else:
        return HttpResponseRedirect(reverse('notLoggedIn'))
