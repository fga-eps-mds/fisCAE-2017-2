from django.conf.urls import url, include
from django.contrib import admin
from merenda import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('acessar_documento.urls', namespace='acessar_documento')),
    url(r'^', include('checklist.urls', namespace='checklist')),
    url(r'^', include('search_school.urls', namespace='search_school')),
    url(r'^', include('agendar_reuniao.urls', namespace='agendar_reuniao')),
    url(r'^', include('user.urls', namespace='user')),
    url(r'^', include('acessar_cartilha.urls', namespace='acessar_cartilha')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),

    url(r'^notLoggedIn/$', views.notLoggedIn, name='notLoggedIn'),     
]


urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

