from django.conf.urls import url, include
from django.contrib import admin
from merenda import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url(r'^', include('checklist.urls', namespace='checklist')),
    url(r'^', include('search_school.urls', namespace='search_school')),
    url(r'^', include('acessar_documento.urls', namespace='acessar_documento')),

    url(r'^$', views.index, name='index'),

    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),

    url(
        r'^view_pdf_cae/CartilhaCAE.pdf$',
        views.view_pdf_cae,
        name='view_pdf_cae'
    ),
    url(r'^index', views.home, name='home'),
    url(r'^findSchool', views.findSchool, name='findSchool'),
    url(r'^formSelect', views.formSelect, name='formSelect'),
    url(r'^tecForm', views.tecForm, name='tecForm'),
    url(r'^viewChecklist', views.viewChecklist, name='viewChecklist'),
    url(r'^indexScheduleMeeting', views.indexScheduleMeeting,
        name='indexScheduleMeeting'),
    url(r'^scheduled', views.scheduled, name='scheduled'),
    url(r'^schedule_delete/(?P<pk>\d+)/$',
        views.schedule_delete, name='schedule_delete'),
    url(r'^formChecklist', views.checklistForm, name='checklistForm'),
    url(r'^answerForm', views.answerForm, name='answerForm'),
    url(r'^edit_schedule/(?P<pk>\d+)/$',
        views.edit_schedule, name='edit_schedule'),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
