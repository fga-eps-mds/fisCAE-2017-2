from django.conf.urls import url
from user import views
from django.contrib import admin
admin.autodiscover()

app_name = 'user'
urlpatterns = [
    url(r'^registro/$', views.register, name='registro'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userEdit/$', views.userEdit, name='userEdit'),
    url(r'^userDelete/(?P<pk>\d+)$', views.userDelete, name='userDelete'),
    url(r'^reset_password/$', views.reset_password, name='reset_password'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^password_sucess/$', views.password_sucess, name='password_sucess'),
    url(r'^listRequests/$', views.listRequests, name='listRequests'),
    url(r'^addAdmin/$', views.addAdmin, name='addAdmin'),
    url(r'^addPresident/$', views.addPresident, name='addPresident'),
]
