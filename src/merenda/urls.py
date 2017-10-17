from django.conf.urls import url, include
from django.contrib import admin
from merenda import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^$', views.index, name='index'),
    url(
        r'^view_pdf_cae/CartilhaCAE.pdf$',
        views.view_pdf_cae,
        name='view_pdf_cae'
    ),
    url(r'^home', views.home, name='home'),
    url(r'^findSchool', views.findSchool, name='findSchool'),
    url(r'^formSelect', views.formSelect, name='formSelect'),
    url(r'^tecForm', views.tecForm, name='tecForm'),
    url(r'^viewChecklist', views.viewChecklist, name='viewChecklist'),
    url(r'^Success', views.Success, name='Success'),
    url(r'^indexScheduleMeeting', views.indexScheduleMeeting, name='indexScheduleMeeting'),
    url(r'^scheduled', views.scheduled, name='scheduled'),
    url(r'^schedule_delete/(?P<pk>\d+)/$', views.schedule_delete, name='schedule_delete'),
    url(r'^formChecklist', views.checklistForm, name='checklistForm'),
    url(r'^answerForm', views.answerForm, name='answerForm'),

]
