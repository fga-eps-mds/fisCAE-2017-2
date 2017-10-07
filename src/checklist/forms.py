from django import forms
from django.forms import ModelForm

from .models import Answer
from .models import Checklist


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)
        widgets = {'answer': forms.RadioSelect}


class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist
        fields = ('checklist_type',)
        widgets = {'checklist_type': forms.RadioSelect}
