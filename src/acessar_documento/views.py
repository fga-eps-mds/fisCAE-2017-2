from django.shortcuts import render
from django.shortcuts import HttpResponse
from os import listdir
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm
from django.contrib import messages


def viewpdf(request, pk):
    fs = FileSystemStorage()
    with fs.open(pk) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename='
        return response
    pdf.close()


def upload_file(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        arq = form.save(commit=False)
        arq.arquivo = request.FILES['arquivo']
        arq.title = request.POST['title']
        arq.save()
        form = UploadFileForm()
        messages.add_message(
                request,
                messages.SUCCESS,
                'Arquivo adicionado com sucesso!'
                )
    return render(request, 'upload_file.html', {'form': form})


def documentsAll(request):
    lista = listdir('media')
    return render(request, 'documentsAll.html', {'lista': lista})
