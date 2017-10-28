from django.conf.urls import url
from search_school import views


app_name = 'search_school'
urlpatterns = [
    url(r'^searchSchool/$', views.search, name='searchSchool'),
    url(r'^schoolForm/$', views.schoolForm, name='schoolForm'),
    url(r'^redirectSchool/$', views.redirectSchool, name='redirectSchool'),
    url(r'^notLoggedIn/$', views.notLoggedIn, name='notLoggedIn'),
]
