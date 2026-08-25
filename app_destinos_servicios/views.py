from django.shortcuts import render
from django.shortcuts import redirect

from .forms import DestinoForm, ServicioForm
from .models import Destino, Servicio


def destinos(request):
    form = DestinoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app_destinos_servicios:lista_destinos')
    return render(request, 'app_destinos_servicios/destinos.html', {'form': form})

def servicios(request):
    form = ServicioForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('app_destinos_servicios:lista_servicios')
    return render(request, 'app_destinos_servicios/servicios.html', {'form': form})


def lista_destinos(request):
    return render(request, 'app_destinos_servicios/lista_destinos.html', {
        'destinos': Destino.objects.order_by('-id'),
    })


def lista_servicios(request):
    return render(request, 'app_destinos_servicios/lista_servicios.html', {
        'servicios': Servicio.objects.order_by('-id'),
    })