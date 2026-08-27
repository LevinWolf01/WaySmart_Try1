from django.urls import path
from . import views

urlpatterns = [
    path('rutas/', views.rutas_view, name='rutas'),
    path('asignaciones/', views.asignaciones_view, name='asignaciones'),
]