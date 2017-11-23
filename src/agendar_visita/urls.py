from django.conf.urls import url
from agendar_visita import views


app_name = 'agendar_visita'
urlpatterns = [
    url(
        r'indexScheduleVisit',
        views.indexScheduleVisit,
        name='indexScheduleVisit'
        ),
    url(r'visitScheduleds', views.sceduled, name='visitScheduled'),
    url(
        r'scheduleVisitDelete/(?P<pk>\d+)/$',
        views.scheduleVisitDelete,
        name='scheduleVisitDelete'
        ),
    url(r'editVisit/(?P<pk>\d+)/$', views.editVisit, name='editVisit'),
]
