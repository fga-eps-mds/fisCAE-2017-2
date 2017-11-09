from django.conf.urls import url
from checklist import views


app_name = 'checklist'
urlpatterns = [
    url(r'^success', views.success, name='success'),
    url(r'^checklistForm', views.checklistForm, name='checklistForm'),
    url(r'^answerForm', views.answerForm, name='answerForm'),
    url(r'^showAnswers', views.showAnswers, name='showAnswers')

]
