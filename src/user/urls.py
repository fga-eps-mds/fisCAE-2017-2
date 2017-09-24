from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^registro/$', views.show_user_form, name='registro'),
    url(r'^login/$', views.login, name='login'),
]
