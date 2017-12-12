from django.conf.urls import url
from . import views

app_name = 'acessar_documento'
urlpatterns = [
    url(r'^adicionar-arquivo', views.upload_file, name='upload_file'),
    url(r'^documentos', views.documentsAll, name='documentsAll'),
    url(r'^visualizar/(?P<pk>[^/]+)/', views.viewpdf, name='viewpdf'),
]
