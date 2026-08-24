from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_modelos, name='lista_modelos'),
    path('crear/', views.crear_modelo, name='crear_modelo'),
    path('editar/<int:pk>/', views.editar_modelo, name='editar_modelo'),
    path('eliminar/<int:pk>/', views.eliminar_modelo, name='eliminar_modelo'),
]