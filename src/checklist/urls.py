from django.conf.urls import url
from checklist import views


app_name = 'checklist'
urlpatterns = [
    url(r'^checklist-finalizado', views.completed, name='completed'),
    url(r'^selecionar-checklist/(?P<id_visit>\d+)/$',
        views.checklistForm,
        name='checklistForm'),
    url(
        r'^responder/(?P<checklist_id>\d+)/$',
        views.answerForm,
        name='answerForm'
        ),
    url(
        r'^visualizar-checklist/([0-9]+)/$',
        views.showAnswers,
        name='showAnswers'
        ),
    url(r'^lista-checklists', views.listSchools, name='listSchools')
]
