from django.conf.urls import url, include
from django.contrib import admin
from merenda import views


urlpatterns = [
    url(r'^', include('checklist.urls', namespace='checklist')),
    url(r'^', include('search_school.urls', namespace='search_school')),

    url(r'^$', views.index, name='index'),

    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),

    url(
        r'^view_pdf_cae/CartilhaCAE.pdf$',
        views.view_pdf_cae,
        name='view_pdf_cae'
    ),
    url(r'^home', views.home, name='home'),
    url(r'^findSchool', views.findSchool, name='findSchool'),
    url(r'^formSelect', views.formSelect, name='formSelect'),
    url(r'^tecForm', views.tecForm, name='tecForm'),
    url(r'^notLoggedIn/$', views.notLoggedIn, name='notLoggedIn'),
]
