from .models import Advisor
from django.contrib.auth.models import User
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth import logout as django_logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from user.forms import AdvisorForm
import smtplib
from random import choice
# from nuvem_civica.services import postUser
import re


def password_sucess(request):
    return render(request, 'password_sucess.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        usuario_id = request.user.id
        user = User.objects.get(id=usuario_id)
        new_password = request.POST['password']
        new_password_confirm = request.POST['password_confirmation']

        if new_password == new_password_confirm:
            user.set_password(request.POST['password'])
            user.save()
            django_logout(request)
            return render(request, 'password_sucess.html')
        else:
            mensagem = 'Senhas incorretas!'
            return render(request, 'change_password.html', {
                'mensagem': mensagem
            })
        return render(request, 'password_sucess.html')        
    return render(request, 'change_password.html')


def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwordtmp = ''
        caracters = '0123456789abcdefghijlmnopqrstuwvxz'
        try:
            mensagem1 = 'Solicitação realizada com sucesso!'
            mensagem2 = 'Uma nova senha foi enviada para o email:'
            mensagem = mensagem1+mensagem2
            usuario = Advisor.objects.get(email=email)
            user = User.objects.get(username=usuario.name)
            for char in range(6):
                passwordtmp += choice(caracters)

            user.set_password(passwordtmp)
            user.save()
            content1 = 'Essa e sua senha temporaria'
            content2 = 'para acessar seu perfil '+passwordtmp
            content = content1+content2
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('fiscaeinfo@gmail.com', 'fiscae2017')
            mail.sendmail('fiscaeinfo@gmail.com', email, content)
            return render(request, 'sucess_reset_password.html', {
                    'usuario': usuario, 'mensagem': mensagem
                })
        except:
            mensagem = 'O email digitado não está cadastrado!'
            return render(request, 'sucess_reset_password.html', {
                'mensagem': mensagem
            })
    return render(request, 'reset_password.html')


def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            error = 'Username ou senha incorretos!'
            context = {'error': error}
            return render(request, 'login.html', context)
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
            error = 'Usuário já existe!'
            context = {'error': error}
            return render(request, 'registro.html', context)
        advisor.name = request.POST['name']
        advisor.email = request.POST['email']
        advisor.cpf = request.POST['cpf']
        advisor.cep = request.POST['cep']
        advisor.bairro = request.POST['bairro']
        advisor.municipio = request.POST.get("municipio", "")
        advisor.uf = request.POST.get("uf", "")
        cep = re.sub(u'[- A-Z a-z]', '', advisor.cep)
        advisor.cep = cep
        advisor.save()
        # Deixar comentado
        """response = postUser(
                        advisor.cep,
                        advisor.email,
                        advisor.name,
                        username,
                        password
                    )
        print(response.status_code, response.reason)"""
        return render(request, 'login.html')
    else:
        return render(request, 'registro.html')


@login_required
def userDelete(request, pk):
    if request.method == 'POST':
        Advisor.objects.filter(id=pk).delete()
        User.objects.filter(id=pk).delete()
        django_logout(request)
        return render(request, 'index.html')
    return render(request, 'userDelete.html')


@login_required
def index(request):
    advisor = Advisor.objects.get(user=request.user)
    return render(request,
                  'checklist/templates/index.html',
                  {'advisor': advisor})


@login_required
def userEdit(request, pk):
    id = pk
    user = get_object_or_404(Advisor, pk=pk)
    form = AdvisorForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if pk == user.id:
            form.save()
            return redirect('../../')
    return render(request, 'userEdit.html', {'form': form, 'id': id})
