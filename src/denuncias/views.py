from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone

from .models import Denunciation


def denunciations(request):
    if request.method == 'POST':
        denunciation = Denunciation()
        denunciation.user_name = request.POST['user_name']
        denunciation.email = request.POST['email']
        denunciation.description = request.POST['description']
        denunciation.save()
        return HttpResponseRedirect(reverse('denuncias:denunciations'))
    


    return render(request, 'denuncias/denunciations.html')