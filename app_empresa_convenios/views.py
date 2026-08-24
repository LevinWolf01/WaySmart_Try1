from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa, Convenios
from django.forms import modelform_factory

# Formularios automáticos basados en los modelos
EmpresaForm = modelform_factory(Empresa, exclude=['Fecha_validacion', 'Observacion_rechazo'])
ConvenioForm = modelform_factory(Convenios, fields='__all__')

def gestion_empresas(request):
    editar_id = request.GET.get('editar')
    eliminar_id = request.GET.get('eliminar')
    
    instance = None
    if editar_id:
        instance = get_object_or_404(Empresa, pk=editar_id)
        
    if eliminar_id:
        empresa = get_object_or_404(Empresa, pk=eliminar_id)
        empresa.delete()
        return redirect('empresa_view')
        
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('empresa_view')
    else:
        form = EmpresaForm(instance=instance)
        
    empresas = Empresa.objects.all()
    return render(request, 'empresa.html', {'form': form, 'empresas': empresas})


def gestion_convenios(request):
    editar_id = request.GET.get('editar')
    eliminar_id = request.GET.get('eliminar')
    
    instance = None
    if editar_id:
        instance = get_object_or_404(Convenios, pk=editar_id)
        
    if eliminar_id:
        convenio = get_object_or_404(Convenios, pk=eliminar_id)
        convenio.delete()
        return redirect('convenio_view')
        
    if request.method == 'POST':
        form = ConvenioForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('convenio_view')
    else:
        form = ConvenioForm(instance=instance)
        
    convenios = Convenios.objects.all()
    return render(request, 'convenios.html', {'form': form, 'convenios': convenios}) # <-- Corregido a convenios.html