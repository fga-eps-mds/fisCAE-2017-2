from django.shortcuts import render
from .models import Advisor
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return HttpResponseRedirect(reverse('index'))


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return HttpResponseRedirect(reverse('index'))


def register(request):
    try:
        if request.method == 'POST':
            advisor = Advisor()
            advisor.name = request.POST['name']
            advisor.phone = request.POST['phone']
            advisor.email = request.POST['email']
            advisor.cpf = request.POST['cpf']
            # endereço
            advisor.cep = request.POST['cep']
            advisor.descricao = request.POST['descricao']
            advisor.bairro = request.POST['bairro']
            advisor.municipio = request.POST['municipio']
            advisor.uf = request.POST['uf']
            # endereço
            password = request.POST['password']
            username = request.POST['username']
            user = User.objects.create_user(username=username,
                                            password=password)
            advisor.user = user
            advisor.save()
            return render(request, 'login.html')
        else:
            return render(request, 'registro.html')
    except:
        return render(request, 'registro.html')


@login_required
def index(request):
    advisor = Advisor.objects.get(user=request.user)
    return render(request,
                  'checklist/templates/index.html',
                  {'advisor': advisor})
