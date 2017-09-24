from django.shortcuts import render
from .models import Advisor
from django.contrib.auth.models import User
# Create your views here.


def show_user_form(request):
    pass


def login(request):
    #if request.method == 'POST':
      #  user = authenticate(username = request.POST['username'], password = request.POST['password'])
        
     #   return render(request, 'login.html')
    pass

def register(request):
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
        password = request.POST['password']
        username = request.POST['username']
        user = User.objects.create_user(username=username, password=password)
        advisor.user = user
        advisor.save()
        return render(request, 'registro.html')
    else:
        return render(request, 'registro.html')
