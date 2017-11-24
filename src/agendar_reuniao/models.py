from django.db import models

 
class Agendamento(models.Model):
    data = models.TextField()
    horario = models.TextField()
    local = models.TextField()
    tema = models.TextField()
    observacoes = models.TextField()
    nome_cae_schedule = models.CharField(max_length=50)

    @staticmethod
    def agendamentos(request):
        visitas = []
        visitas = Agendamento.objects.all()
        return visitas

