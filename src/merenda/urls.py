"""merenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from merenda import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^view_pdf_cae/CartilhaCAE.pdf$', views.view_pdf_cae, name='view_pdf_cae'),
    url(r'^check', views.check, name='check'),
    url(r'^home', views.home, name='home'),
    url(r'^findSchool', views.findSchool, name='findSchool'),
    url(r'^formSelect', views.formSelect, name='formSelect'),
    url(r'^tecForm', views.tecForm, name='tecForm'),
    url(r'^viewChecklist', views.viewChecklist, name='viewChecklist'),
    url(r'^Success', views.Success, name='Success'),
    url(r'^upload_file', views.upload_file, name='upload_file'),
    url(r'^documentsAll', views.documentsAll, name='documentsAll'),
    url(r'^viewpdf', views.viewpdf, name='viewpdf'),
    
   
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
    
