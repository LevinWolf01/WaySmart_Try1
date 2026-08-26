from django.shortcuts import render, redirect
from .models import Asignacion, Ruta

# PÁGINA 1: Formulario + Tabla de Asignaciones
def asignaciones_view(request):
    if request.method == 'POST':
        servicios_servicios_id = request.POST.get('servicios_servicios_id')
        servicio_id = request.POST.get('servicio_id')
        repartidor_id = request.POST.get('repartidor_id')
        estado = request.POST.get('estado')

        Asignacion.objects.create(
            servicios_servicios_id=servicios_servicios_id,
            servicio_id=servicio_id,
            repartidor_id=repartidor_id,
            estado=estado
        )
        return redirect('asignaciones')

    asignaciones = Asignacion.objects.all()
    return render(request, 'app_rutas_asignaciones/asignaciones.html', {'asignaciones': asignaciones})


# PÁGINA 2: Formulario + Tabla de Rutas
def rutas_view(request):
    if request.method == 'POST':
        asignacion_id = request.POST.get('asignacion_id')
        tipo_ruta = request.POST.get('tipo_ruta')
        tiempo_estimado_min = request.POST.get('tiempo_estimado_min')
        polyline_json = request.POST.get('polyline_json', '{}')
        seleccionada = request.POST.get('seleccionada') == 'on'

        asignacion_obj = Asignacion.objects.get(pk=asignacion_id)
        Ruta.objects.create(
            asignacion=asignacion_obj,
            tipo_ruta=tipo_ruta,
            tiempo_estimado_min=tiempo_estimado_min,
            polyline_json=polyline_json,
            seleccionada=seleccionada
        )
        return redirect('rutas')

    rutas = Ruta.objects.all()
    asignaciones = Asignacion.objects.all()
    return render(request, 'app_rutas_asignaciones/rutas.html', {'rutas': rutas, 'asignaciones': asignaciones})