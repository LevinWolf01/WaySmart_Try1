from django.shortcuts import render

from .models import Documento, Usuario

# Create your views here.

def usuario_view(request):
    usuarios = Usuario.objects.all().order_by('-fecha_creacion')
    return render(request, 'usuario.html', {'usuarios': usuarios})

def documento_view(request):
    documentos = Documento.objects.select_related('usuario').all().order_by('-fecha_subida')
    return render(request, 'documento.html', {'documentos': documentos})
