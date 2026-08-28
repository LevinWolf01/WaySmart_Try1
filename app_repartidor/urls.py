from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_repartidores, name='lista_repartidores'),
    path('crear/', views.crear_repartidor, name='crear_repartidor'),
    path('editar/<int:pk>/', views.editar_repartidor, name='editar_repartidor'),
    path('eliminar/<int:pk>/', views.eliminar_repartidor, name='eliminar_repartidor'),
]