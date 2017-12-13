from django import forms
from django.forms import ModelForm

from .models import Observations
from .models import Answer
from .models import Checklist


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)
        labels = {'answer': ('')}
        widgets = {'answer': forms.RadioSelect}


class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist
        fields = ('checklist_type',)
        labels = {'checklist_type': ('')}
        widgets = {'checklist_type': forms.RadioSelect}


class ObservationsForm(forms.ModelForm):
    class Meta:
        model = Observations
        fields = ['observation', 'images']
