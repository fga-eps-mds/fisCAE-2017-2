from django.forms import ModelForm
from user.models import Advisor

class AdvisorForm(ModelForm):
    class Meta:
        model = Advisor
        exclude = ["user"]
