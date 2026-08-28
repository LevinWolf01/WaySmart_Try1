from django.urls import path

from . import views

urlpatterns = [
    path('waysmart/pago/', views.pagos, name='pago'),
    path(
        'waysmart/pago/<int:id>/',
        views.detalle_pago,
        name='detalle_pago',
    ),
    path(
        'waysmart/pago/<int:id>/eliminar/',
        views.eliminar_pago,
        name='eliminar_pago',
    ),

    path(
        'waysmart/seguimientogeo/',
        views.seguimientogeo,
        name='seguimientogeo',
    ),
    path(
        'waysmart/seguimientogeo/<int:id>/',
        views.detalle_seguimiento,
        name='detalle_seguimiento',
    ),
    path(
        'waysmart/seguimientogeo/<int:id>/eliminar/',
        views.eliminar_seguimiento,
        name='eliminar_seguimiento',
    ),
]