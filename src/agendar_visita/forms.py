from django.forms import ModelForm, Textarea
from .models import ScheduleVisit


class VisitForm(ModelForm):
    class Meta:
        model = ScheduleVisit
        exclude = ['schoolName', 'schoolCode']

        widgets = {
            'date': Textarea(attrs={'cols': 20, 'rows': 1}),
            'time': Textarea(attrs={'cols': 20, 'rows': 1}),
            'members': Textarea(attrs={'cols': 20, 'rows': 1}),
        }
