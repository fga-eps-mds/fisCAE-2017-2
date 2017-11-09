from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone


def denunciations(request):
    
    return render(request, 'denunciations.html')