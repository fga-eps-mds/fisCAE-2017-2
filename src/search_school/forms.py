from django import forms


class SchoolForm(forms.Form):
    schools = []

    def __init__(self, schoolsList):
        self.schools = schoolsList

    fields = ('schools',)
    widgets = {'schools': forms.RadioSelect}
