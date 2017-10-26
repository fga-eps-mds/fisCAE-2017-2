from django.conf.urls import url
from merenda import views


app_name = 'acessar_cartilha'
urlpatterns = [
    url(
        r'^view_pdf_cae/CartilhaCAE.pdf$',
        views.view_pdf_cae,
        name='view_pdf_cae'
    ),
]
