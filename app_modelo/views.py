from django.shortcuts import render
from .models import Modelo

def lista_modelos(request):
    modelos = Modelo.objects.all()
    return render(request, 'app_modelo/lista_modelos.html', {'modelos': modelos})