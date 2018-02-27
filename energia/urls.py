from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'$^', views.inserirDados),
    url(r'^consumo_energia/$', views.consumoEnergia, name='consumo_energia'),
]
