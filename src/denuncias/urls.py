from django.conf.urls import url
from denuncias import views


app_name = 'denuncias'
urlpatterns = [
    url(r'^denunciations', views.denunciations, name='denunciations'),
]
