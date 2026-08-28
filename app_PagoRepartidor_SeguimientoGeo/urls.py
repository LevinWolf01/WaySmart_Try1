from django.urls import path

from . import views

urlpatterns = [
    path('wasmart/pago/', views.pagos, name='pago'),
    path(
        'wasmart/pago/<int:id>/',
        views.detalle_pago,
        name='detalle_pago',
    ),
    path(
        'wasmart/pago/<int:id>/eliminar/',
        views.eliminar_pago,
        name='eliminar_pago',
    ),

    path(
        'wasmart/seguimientogeo/',
        views.seguimientogeo,
        name='seguimientogeo',
    ),
    path(
        'wasmart/seguimientogeo/<int:id>/',
        views.detalle_seguimiento,
        name='detalle_seguimiento',
    ),
    path(
        'wasmart/seguimientogeo/<int:id>/eliminar/',
        views.eliminar_seguimiento,
        name='eliminar_seguimiento',
    ),
]