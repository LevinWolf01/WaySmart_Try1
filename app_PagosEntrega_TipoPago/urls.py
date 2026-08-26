from django.urls import path
from . import views

urlpatterns = [
    path('pagos/', views.pagos_index, name='pagos_index'),
]