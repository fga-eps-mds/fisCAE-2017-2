from django.shortcuts import render
from .models import Advisor
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth import logout as django_logout
from django.urls import reverse
from django.http import HttpResponseRedirect


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


def register(request):
    if request.method == 'POST':
        advisor = Advisor()
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username,
                                            password=password)
            advisor.user = user
        except:
            return render(request, 'registroException.html')
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
        advisor.save()
        return render(request, 'login.html')
    else:
        return render(request, 'registro.html')
