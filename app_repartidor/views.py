from django.shortcuts import render, redirect, get_object_or_404
from .models import Repartidor

def lista_repartidores(request):
    repartidores = Repartidor.objects.all()
    return render(request, 'app_repartidor/lista_repartidores.html', {'repartidores': repartidores})

def crear_repartidor(request):
    if request.method == 'POST':
        nuevo = Repartidor()
        nuevo.Nombres = request.POST.get('Nombres')
        nuevo.Apellidos = request.POST.get('Apellidos')
        nuevo.Nro_Identificacion = request.POST.get('Nro_Identificacion')
        nuevo.Telefono = request.POST.get('Telefono')
        nuevo.Estado = request.POST.get('Estado')
        nuevo.Observacion_Rechazo = request.POST.get('Observacion_Rechazo')
        nuevo.save()
        return redirect('lista_repartidores')
    return render(request, 'app_repartidor/formulario_repartidor.html')

def editar_repartidor(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    if request.method == 'POST':
        repartidor.Nombres = request.POST.get('Nombres')
        repartidor.Apellidos = request.POST.get('Apellidos')
        repartidor.Nro_Identificacion = request.POST.get('Nro_Identificacion')
        repartidor.Telefono = request.POST.get('Telefono')
        repartidor.Estado = request.POST.get('Estado')
        repartidor.Observacion_Rechazo = request.POST.get('Observacion_Rechazo')
        repartidor.save()
        return redirect('lista_repartidores')
    return render(request, 'app_repartidor/formulario_repartidor.html', {'repartidor': repartidor})

def eliminar_repartidor(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    if request.method == 'POST':
        repartidor.delete()
        return redirect('lista_repartidores')
    return render(request, 'app_repartidor/confirmar_eliminar_repartidor.html', {'repartidor': repartidor})