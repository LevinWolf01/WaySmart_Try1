from django.shortcuts import render
from .models import Pagos_repartidor  # Asegúrate de importar tu nuevo modelo

def crear_pagos(request):
    # 1. Creamos el objeto con datos económicos quemados de prueba
    nuevo_pago = Pagos_repartidor(
        id_Repartidor = 45,                  # ID numérico del repartidor
        monto_total_generado = 150000.00,    # Dinero total que hizo el repartidor
        comision_plataforma = 30000.00,      # Comisión que se queda la app
        monto_neto = 120000.00,               # Ganancia real del repartidor
        estado = 'pendiente'                 # Estado inicial usando una de las opciones
    )
    
    # 2. bulk_create requiere una lista entre corchetes []
    Pagos_repartidor.objects.bulk_create([nuevo_pago])
    
    # 3. Traemos todos los registros de la tabla para pintarlos en el HTML
    pagos_db = Pagos_repartidor.objects.all()
    
    # 4. Enviamos los datos al HTML (siguiendo tu lógica de nombres)
    return render(request, 'pagos_repartidor/pagos.html', {
        'pagos': pagos_db,
        'listapagos': pagos_db
    })
