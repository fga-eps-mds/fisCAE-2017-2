from django.forms import ModelForm
from .models import Answer
from .models import Checklist


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ('answer',)


class ChecklistForm(ModelForm):
    class Meta:
        model = Checklist
        fields = ('checklist_type',)
