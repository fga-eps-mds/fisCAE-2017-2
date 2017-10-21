from django.forms import ModelForm
from agendar_reuniao.models import Agendamento

class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        exclude = [""]
