from django.urls import path
from . import views

urlpatterns = [
    path('empresas/', views.gestion_empresas, name='empresa_view'),
    path('convenios/', views.gestion_convenios, name='convenio_view'),
]