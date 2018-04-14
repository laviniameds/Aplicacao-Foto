from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'$^', views.inserirDados),
    url(r'^view_tabelas/$', views.consumoEnergia, name='view_tabelas'),
]
