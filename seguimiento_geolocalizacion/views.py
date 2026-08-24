from django.shortcuts import render, redirect
from .models import Seguimiento_Geolocalizacion
from django.http import HttpResponse

# Create your views here.
def crear_seguimiento(request):

    seguimiento = Seguimiento_Geolocalizacion(
        id_Repartidor = 45,                # ID numérico del repartidor
        latitud = 2.4448,                  # Coordenada real (ej. Popayán, Colombia)
        longitud = -76.6147,               # Coordenada real
        velocidad = 25                     # Velocidad en km/h
    )
        # 2. bulk_create requiere una lista entre corchetes []
    Seguimiento_Geolocalizacion.objects.bulk_create([seguimiento])
    
    # 3. Traemos todos los registros para pintarlos en el HTML
    seguimientos_db = Seguimiento_Geolocalizacion.objects.all()
    
    # 4. Enviamos los datos al HTML (usamos 'seguimientos' para el bucle principal)
    return render(request, 'seguimiento_geolocalizacion/bienvenida.html', {
        'seguimientos': seguimientos_db,
        'listaseguimientos': seguimientos_db
    })