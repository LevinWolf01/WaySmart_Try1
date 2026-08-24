from django.urls import path
from . import views

urlpatterns = [
    path('rutas/', views.rutas, name='rutas'),
    path('asignaciones/', views.asignaciones, name='asignaciones'),
]
