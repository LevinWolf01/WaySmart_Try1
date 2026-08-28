from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.usuario_view, name='usuario'),
    path('documento/', views.documento_view, name='documento'),
]
