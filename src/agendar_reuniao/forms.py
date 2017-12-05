from django.forms import ModelForm
from django.forms import Textarea
from agendar_reuniao.models import Agendamento


class AgendamentoForm(ModelForm):
    class Meta:
        model = Agendamento
        exclude = ['tema', 'nome_cae_schedule']
        widgets = {
            'data': Textarea(attrs={
                'cols': 20,
                'rows': 1
            }),
            'horario': Textarea(attrs={
                'cols': 20,
                'rows': 1
            }),
            'local': Textarea(attrs={
                'cols': 20,
                'rows': 1
            }),
            'observacoes': Textarea(attrs={
                'cols': 20,
                'rows': 1
            }),
        }