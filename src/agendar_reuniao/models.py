from django.db import models

 
class Agendamento(models.Model):
    data = models.TextField()
    horario = models.TextField()
    local = models.TextField()
    tema = models.TextField()
    observacoes = models.TextField()

    @staticmethod
    def agendamentos(request):
        visitas = []
        visitas = Agendamento.objects.all()
        return visitas
