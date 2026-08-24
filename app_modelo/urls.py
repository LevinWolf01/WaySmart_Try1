from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_modelos, name='lista_modelos'),
]