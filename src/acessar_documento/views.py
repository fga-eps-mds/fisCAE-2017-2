from django.shortcuts import render
from django.shortcuts import HttpResponse
from os import listdir
from django.core.files.storage import FileSystemStorage
from .forms import UploadFileForm


def viewpdf(request, pk):
    fs = FileSystemStorage()
    # with fs.open(pk+'.pdf') as pdf:
    with fs.open(pk) as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename='
        pdf.close()
        return response


def upload_file(request):
    form = UploadFileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        arq = form.save(commit=False)
        arq.arquivo = request.FILES['arquivo']
        arq.title = request.POST['title']
        arq.save()
        # return render(request, 'documentsAll.html')
    return render(request, 'upload_file.html', {'form': form})


def documentsAll(request):
    try:
        lista = listdir('media')
    except:
        lista = listdir('app/media')
    return render(request, 'documentsAll.html', {'lista': lista})
    # lista = Arquivos.arquivosSalvos()
    # return render(request,'documentsAll.html',{'lista':lista})
