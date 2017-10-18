from django.conf.urls import url
from search_school import views


app_name = 'search_school'
urlpatterns = [
    url(r'^searchSchool/$', views.search, name='searchSchool'),
]
