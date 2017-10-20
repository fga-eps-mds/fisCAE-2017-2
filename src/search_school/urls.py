from django.conf.urls import url
from search_school import views


app_name = 'search_school'
urlpatterns = [
    url(r'^searchSchool/$', views.search, name='searchSchool'),
    url(r'^schoolForm/$', views.schoolForm, name='schoolForm'),
    url(r'^successSchool/$', views.successSchool, name='successSchool'),
    url(r'^notLoggedIn/$', views.notLoggedIn, name='notLoggedIn'),
]
