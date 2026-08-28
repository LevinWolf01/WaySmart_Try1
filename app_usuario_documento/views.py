from django.shortcuts import render

from .forms import DocumentoForm, UsuarioForm
from .models import Documento, Usuario

# Create your views here.

def usuario_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UsuarioForm()

    usuarios = Usuario.objects.all().order_by('-fecha_creacion')
    return render(request, 'usuario.html', {'usuarios': usuarios, 'form': form})

def documento_view(request):
    if request.method == 'POST':
        form = DocumentoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = DocumentoForm()

    documentos = Documento.objects.select_related('usuario').all().order_by('-fecha_subida')
    return render(request, 'documento.html', {'documentos': documentos, 'form': form})
