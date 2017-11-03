from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^registro/$', views.register, name='registro'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userEdit/(?P<pk>\d+)$', views.userEdit, name='userEdit'),
]
