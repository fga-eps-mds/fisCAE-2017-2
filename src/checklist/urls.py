from django.conf.urls import url
from checklist import views


app_name = 'checklist'
urlpatterns = [
    url(r'^success', views.success, name='success'),
    url(r'^checklistForm/(?P<id_visit>\d+)/$', views.checklistForm, name='checklistForm'),
    url(r'^answerForm', views.answerForm, name='answerForm'),
    # url(
    #     r'^schedule_delete/(?P<pk>\d+)/$',
    #     views.schedule_delete,
    #     name='schedule_delete'
    #     ),
]
