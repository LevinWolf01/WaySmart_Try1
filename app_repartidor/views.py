from django.shortcuts import render
from .models import Repartidor

def lista_repartidores(request):
    repartidores = Repartidor.objects.all()
    return render(request, 'app_repartidor/lista_repartidores.html', {'repartidores': repartidores})