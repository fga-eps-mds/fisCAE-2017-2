from django.conf.urls import url
from django.contrib import admin
from checklist import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^check', views.check, name='check'),
    url(r'^home', views.home, name='home'),
    url(r'^findSchool', views.findSchool, name='findSchool'),
    url(r'^formSelect', views.formSelect, name='formSelect'),
    url(r'^viewChecklist', views.viewChecklist, name='viewChecklist'),
]
