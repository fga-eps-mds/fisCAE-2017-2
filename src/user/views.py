from django.shortcuts import render

# Create your views here.


def show_user_form(request):
    return render(request, 'registro.html')


def login(request):
    return render(request, 'login.html')
