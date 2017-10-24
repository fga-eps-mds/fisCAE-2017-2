from django.conf.urls import url, include
from django.contrib import admin
from merenda import views


urlpatterns = [
    url(r'^', include('checklist.urls', namespace='checklist')),
    url(r'^', include('search_school.urls', namespace='search_school')),

    url(r'^$', views.index, name='index'),

    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),

    url(
        r'^view_pdf_cae/CartilhaCAE.pdf$',
        views.view_pdf_cae,
        name='view_pdf_cae'
    ),
    url(r'^notLoggedIn/$', views.notLoggedIn, name='notLoggedIn'),
    url(r'^home', views.home, name='home'),
    url(r'^Success', views.Success, name='Success'),
    url(r'^indexScheduleMeeting', views.indexScheduleMeeting, name='indexScheduleMeeting'),
    url(r'^scheduled', views.scheduled, name='scheduled'),
    url(r'^schedule_delete/(?P<pk>\d+)/$', views.schedule_delete, name='schedule_delete'),
    url(r'^edit_schedule/(?P<pk>\d+)/$', views.edit_schedule, name='edit_schedule'),
]
