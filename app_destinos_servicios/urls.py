from django.urls import path

from . import views

app_name = 'app_destinos_servicios'

urlpatterns = [
    path('destino/', views.destinos, name='crear_destino'),
    path('destino/lista/', views.lista_destinos, name='lista_destinos'),
    path('servicio/', views.servicios, name='crear_servicio'),
    path('servicio/lista/', views.lista_servicios, name='lista_servicios'),
]