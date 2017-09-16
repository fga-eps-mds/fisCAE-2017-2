from django.shortcuts import render

# Create your views here.
def acessar_cartilha(request):
	return render(request, 'acessar_cartilha.html')
