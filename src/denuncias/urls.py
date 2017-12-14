from django.conf.urls import url
from denuncias import views

app_name = 'denuncias'
urlpatterns = [
    url(r'^denunciar', views.denunciations, name='denunciations'),
]
