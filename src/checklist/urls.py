from django.conf.urls import url
from checklist import views


app_name = 'checklist'
urlpatterns = [
    url(r'^success', views.success, name='success'),
    url(r'^checklistForm/(?P<id_visit>\d+)/$',
        views.checklistForm,
        name='checklistForm'),
    url(r'^answerForm', views.answerForm, name='answerForm'),

]
