from django.conf.urls import url
from agendar_reuniao import views


app_name = 'agendar_reuniao'
urlpatterns = [
    url(
        r'indexScheduleMeeting',
        views.indexScheduleMeeting,
        name='indexScheduleMeeting'
        ),
    url(r'scheduled', views.scheduled, name='scheduled'),
    url(r'schedules', views.schedules, name='schedules'),
    url(
        r'schedule_delete/(?P<pk>\d+)/$',
        views.schedule_delete,
        name='schedule_delete'
        ),
    url(
        r'edit_schedule/(?P<pk>\d+)/$',
        views.edit_schedule,
        name='edit_schedule'
        ),
    url(
        r'notify/',
        views.notify,
        name='notify'
        ),
]
