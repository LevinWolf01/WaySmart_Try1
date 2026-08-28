from django.shortcuts import render

def inicio(request):
    return render(request, 'app_vehiculos_colores/inicio.html') # O la plantilla que uses para inicio

def fn_vehiculo(request):
    return render(request, 'app_vehiculos_colores/vehiculo.html')

def fn_colores(request):
    return render(request, 'app_vehiculos_colores/colores.html')
