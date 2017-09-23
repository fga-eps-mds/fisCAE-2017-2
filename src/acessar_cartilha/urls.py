from django.conf.urls import url
from django.contrib import admin
from acessar_cartilha import views

urlpatterns = [
    url(r'^$', views.access_doc, name='access_doc'),
    url(r'^view_pdf_cae$', views.view_pdf_cae, name='view_pdf_cae')
]
