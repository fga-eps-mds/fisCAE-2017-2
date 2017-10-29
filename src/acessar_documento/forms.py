from django import forms
from .models import Arquivos


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Arquivos
        fields = ['title' , 'arquivo']