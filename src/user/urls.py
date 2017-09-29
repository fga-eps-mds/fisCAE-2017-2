from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^registro/$', views.register, name='registro'),
    url(r'^login/$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout')
]
