from django.conf.urls import url
from django.contrib import admin
from acessar_cartilha import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.acessar_cartilha, name='Acessar Cartilha')
]
