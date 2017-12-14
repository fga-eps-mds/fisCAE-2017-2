from django.conf.urls import url
from agendar_reuniao import views


app_name = 'agendar_reuniao'
urlpatterns = [
    url(
        r'^agendar-reuniao/$',
        views.indexScheduleMeeting,
        name='indexScheduleMeeting'
        ),
    url(r'^reunioes-agendadas/$', views.scheduled, name='scheduled'),
    url(r'eventos/$', views.schedules, name='schedules'),
    url(
        r'deletar-reuniao/(?P<pk>\d+)/$',
        views.schedule_delete,
        name='schedule_delete'
        ),
    url(
        r'editar-reuniao/(?P<pk>\d+)/$',
        views.edit_schedule,
        name='edit_schedule'
        ),
]
