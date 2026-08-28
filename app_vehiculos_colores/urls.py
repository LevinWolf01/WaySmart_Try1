from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('vehiculo/', views.fn_vehiculo, name='vehiculo'),  # o como se llame tu función en views.py
    path('colores/', views.fn_colores, name='colores'),
]

