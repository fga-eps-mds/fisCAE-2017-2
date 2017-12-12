from django.conf.urls import url
from search_school import views


app_name = 'search_school'
urlpatterns = [
    url(r'^pesquisar-escola/$', views.search, name='searchSchool'),
    url(r'^selecionar-escola/$', views.schoolForm, name='schoolForm'),
]
