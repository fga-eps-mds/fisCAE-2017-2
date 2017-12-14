from django.conf.urls import url
from user import views
from django.contrib import admin
admin.autodiscover()

app_name = 'user'
urlpatterns = [
    url(r'^registro/$', views.register, name='registro'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^editar-usuario/$', views.userEdit, name='userEdit'),
    url(r'^deletar-usuário/$', views.userDelete, name='userDelete'),
    url(r'^resetar-senha/$', views.reset_password, name='reset_password'),
    url(r'^alterar-senha/$', views.change_password, name='change_password'),
    url(r'^senha-alterada/$', views.password_sucess, name='password_sucess'),
    url(r'^aprovar-cadastros/$', views.listRequests, name='listRequests'),
    url(r'^cadastrar-administrador/$', views.addAdmin, name='addAdmin'),
    url(r'^cadastrar-presidente/$', views.addPresident, name='addPresident'),
]
