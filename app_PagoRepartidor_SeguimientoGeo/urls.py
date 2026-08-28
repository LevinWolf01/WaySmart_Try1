from django.urls import path

from . import views

urlpatterns = [
    path('wasmart/pago/', views.pagos, name='pago'),
    path(
        'wasmart/seguimientogeo/',
        views.seguimientogeo,
        name='seguimientogeo',
    ),
]