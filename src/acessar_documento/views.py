from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
# Create your views here.
from somewhere import handle_uploaded_file


def documents(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'documents.html')
