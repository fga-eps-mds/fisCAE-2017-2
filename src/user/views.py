from django.contrib.auth.models import User, Permission
from django.contrib.auth import login as django_login, authenticate
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from django.forms import modelformset_factory
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import smtplib
from random import choice
import re
from django.contrib import messages

from .models import Advisor, President
from .forms import AdvisorForm, AdministratorForm
from .forms import PresidentForm, ConfirmUserForm
# from nuvem_civica.services import postUser


def password_sucess(request):
    return render(request, 'password_sucess.html')


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
    return render(request, 'change_password.html')


def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        passwordtmp = ''
        caracters = '0123456789abcdefghijlmnopqrstuwvxz'
        try:
            mensagem1 = 'Solicitação realizada com sucesso! '
            mensagem2 = 'Uma nova senha foi enviada para o email:'
            mensagem = mensagem1 + mensagem2
            usuario = Advisor.objects.get(email=email)
            user = User.objects.get(username=usuario.name)
            for char in range(6):
                passwordtmp += choice(caracters)

            user.set_password(passwordtmp)
            user.save()
            content1 = 'Essa e sua senha temporaria '
            content2 = 'para acessar seu perfil ' + passwordtmp
            content = content1 + content2
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login('noreplayfiscae@gmail.com', 'fiscaeunb')
            mail.sendmail('noreplayfiscae@gmail.com', email, content)
            mail.close()
            return render(request, 'sucess_reset_password.html', {
                'usuario': usuario,
                'mensagem': mensagem
            })
        except:
            mensagem = 'O email digitado não está cadastrado!'
            return render(request, 'sucess_reset_password.html', {
                'mensagem': mensagem
            })
    return render(request, 'reset_password.html')


def login(request):
    context = {'error': ''}
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'])
        if user is not None and user.is_active:
            django_login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            error = 'Login inválido!'
            context = {'error': error}
    return render(request, 'login.html', context)


def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
        return HttpResponseRedirect(reverse('index'))


def setAdvisorPerm(user):
    content_type = ContentType.objects.get_for_model(Advisor)
    advisor_perm = Permission.objects.get(codename='advisor',
                                          content_type=content_type)
    user.user_permissions.add(advisor_perm)


def setCaeType(person):
    if(person.tipo_cae == 'Municipal'):
        person.nome_cae = ('CAE' + ' ' + person.tipo_cae +
                           ' ' + person.municipio)
    else:
        person.nome_cae = 'CAE' + ' ' + person.tipo_cae + ' ' + person.uf


def set_user(request, email):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(
        username=username, password=password, email=email)
    return user


def set_person(request, person, email):
    person.name = request.POST['name']
    person.email = email
    person.cpf = request.POST['cpf']
    person.cep = request.POST['cep']
    person.bairro = request.POST['bairro']
    person.municipio = request.POST['municipio']
    person.uf = request.POST['uf']
    cep = re.sub(u'[- A-Z a-z]', '', person.cep)
    person.cep = cep
    person.tipo_cae = request.POST['tipo_cae']


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = set_user(request, email)
            # Deixar comentado
            """response = postUser(
                            advisor.cep,
                            advisor.email,
                            advisor.name,
                            username,
                            password
                        )
            print(response.status_code, response.reason)"""

        except IntegrityError:
            error = 'Registro inválido!'
            context = {'error': error}
            return render(request, 'registro.html', context)
        person = Advisor()
        setAdvisorPerm(user)
        User.objects.filter(pk=user.id).update(is_active=False)
        set_person(request, person, email)
        setCaeType(person)
        person.user = user
        person.save()
        return render(request, 'login.html')
    else:
        return render(request, 'registro.html')


def userDelete(request):
    pk = request.user.id
    if request.method == 'POST':
        Advisor.objects.filter(id=pk).delete()
        User.objects.filter(id=pk).delete()
        django_logout(request)
        return redirect('index')
    return render(request, 'userDelete.html')


@login_required
def index(request):
    advisor = Advisor.objects.get(user=request.user)
    return render(request, 'checklist/templates/index.html', {
        'advisor': advisor
    })


@login_required
def userEdit(request):
    try:
        user = Advisor.objects.get(user_id=request.user.id)
        formNotPost = AdvisorForm(instance=user)
        formPost = AdvisorForm(request.POST, instance=user)
    except Advisor.DoesNotExist:
        formPost = None
        formNotPost = None
    if request.method == 'POST':
        form = formPost
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = formNotPost
    return render(request, 'userEdit.html', {'form': form})


@login_required
@permission_required('user.president')
def listRequests(request):
    presidents = President.objects.all()
    presidents_ids = presidents.values_list('advisor_ptr_id', flat=True)
    advisors = Advisor.objects.all().exclude(person_ptr_id__in=presidents_ids)
    advisors_id = advisors.values_list('user_id', flat=True)
    users = User.objects.filter(id__in=advisors_id, is_active=False)

    if users is None:
        context = {'avisors': 'None'}
        return render(request, 'listRequests.html', context)

    else:
        UserFormSet = modelformset_factory(User, form=ConfirmUserForm, extra=0)
        if request.method == 'POST':
            formset = UserFormSet(request.POST, queryset=users)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse('index'))

        else:
            formset = UserFormSet(queryset=users)

        context = {'formset': formset}
    return render(request, 'listRequests.html', context)


@login_required
@permission_required('user.administrator')
def addAdmin(request):
    if request.method == 'POST':
        form = AdministratorForm(request.POST)
        saveForm = form.save(commit=True)
        if saveForm:
            form = AdministratorForm()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Usuário cadastrado com sucesso!'
            )
    else:
        form = AdministratorForm()
    return render(request, 'addAdmin.html', {'form': form})


@login_required
@permission_required('user.administrator')
def addPresident(request):
    if request.method == 'POST':
        form = PresidentForm(request.POST)
        saveForm = form.save(commit=True)
        if saveForm:
            form = PresidentForm()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Usuário cadastrado com sucesso!'
            )
    else:
        form = PresidentForm()
    return render(request, 'addPresident.html', {'form': form})
