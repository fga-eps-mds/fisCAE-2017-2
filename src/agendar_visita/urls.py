from django.conf.urls import url
from agendar_visita import views


app_name = 'agendar_visita'
urlpatterns = [
    url(
        r'^agendar-visita/$',
        views.indexScheduleVisit,
        name='indexScheduleVisit'
        ),
    url(r'^visitas-agendadas/$', views.sceduled, name='visitScheduled'),
    url(
        r'deletar-visita/(?P<pk>\d+)/$',
        views.scheduleVisitDelete,
        name='scheduleVisitDelete'
        ),
    url(r'editar-visita/(?P<pk>\d+)/$', views.editVisit, name='editVisit'),
]
