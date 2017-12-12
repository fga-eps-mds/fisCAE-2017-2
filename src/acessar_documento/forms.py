from django import forms
from django.forms import Textarea
from .models import Arquivos


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Arquivos
        fields = ['title', 'arquivo']
        widgets = {
            'title': Textarea(attrs={
                'cols': 20,
                'rows': 1
            }),
        }
