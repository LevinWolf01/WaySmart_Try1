from django.shortcuts import render, redirect, get_object_or_404
from .models import Modelo

def lista_modelos(request):
    modelos = Modelo.objects.all()
    return render(request, 'app_modelo/lista_modelos.html', {'modelos': modelos})

def crear_modelo(request):
    if request.method == 'POST':
        nuevo = Modelo()
        nuevo.Marca = request.POST.get('Marca')
        nuevo.Nombre_Modelo = request.POST.get('Nombre_Modelo')
        nuevo.Color = request.POST.get('Color')
        nuevo.Año = request.POST.get('Año')
        nuevo.Placa = request.POST.get('Placa')
        nuevo.save()
        return redirect('lista_modelos')
    return render(request, 'app_modelo/formulario_modelo.html')

def editar_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        modelo.Marca = request.POST.get('Marca')
        modelo.Nombre_Modelo = request.POST.get('Nombre_Modelo')
        modelo.Color = request.POST.get('Color')
        modelo.Año = request.POST.get('Año')
        modelo.Placa = request.POST.get('Placa')
        modelo.save()
        return redirect('lista_modelos')
    return render(request, 'app_modelo/formulario_modelo.html', {'modelo': modelo})

def eliminar_modelo(request, pk):
    modelo = get_object_or_404(Modelo, pk=pk)
    if request.method == 'POST':
        modelo.delete()
        return redirect('lista_modelos')
    return render(request, 'app_modelo/confirmar_eliminar.html', {'modelo': modelo})