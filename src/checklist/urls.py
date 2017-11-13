from django.conf.urls import url
from checklist import views


app_name = 'checklist'
urlpatterns = [
    url(r'^success', views.success, name='success'),
    url(r'^completed', views.completed, name='completed'),
    url(r'^checklistForm/(?P<id_visit>\d+)/$',
        views.checklistForm,
        name='checklistForm'),
    url(r'^answerForm/(?P<checklist_id>\d+)/$',
        views.answerForm,
        name='answerForm'),
    url(r'^visitsSchool', views.visitsSchool, name='visitsSchool'),
    url(r'^showAnswers/([0-9]+)/$', views.showAnswers, name='showAnswers'),
    url(r'^listSchools', views.listSchools, name='listSchools')
]
