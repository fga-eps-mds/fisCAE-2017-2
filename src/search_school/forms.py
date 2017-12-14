from django import forms


class SchoolForm(forms.Form):
    def __init__(self, *args, **kwargs):
        schools = kwargs.pop('schools')
        super(SchoolForm, self).__init__(*args, **kwargs)
        self.fields['school'] = forms.ChoiceField(
            choices=[(str(s), str(s)) for s in schools],
            widget=forms.RadioSelect
        )
