from django.contrib import admin
from django.urls import path
from . import views

app_name = "app_vehiculos_colores"

urlpatterns = [
    path("colores/", views.colores, name="colores"),
    path("vehiculos/", views.vehiculos, name="vehiculos"),
]
