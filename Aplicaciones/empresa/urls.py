# empresa/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/alerta/', views.recibir_alerta, name='recibir_alerta'),
    path('api/listar-alertas/', views.listar_alertas, name='listar_alertas'),
]
