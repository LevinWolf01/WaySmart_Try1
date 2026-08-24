from django.shortcuts import render
from .models import Ruta, Asignacion


def rutas(request):
    rutas = Ruta.objects.all()
    return render(request, 'app_rutas_asignaciones/rutas.html', {
        'rutas': rutas
    })


def asignaciones(request):
    asignaciones = Asignacion.objects.all()
    return render(request, 'app_rutas_asignaciones/asignaciones.html', {
        'asignaciones': asignaciones
    })
