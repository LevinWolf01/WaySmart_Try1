from django.db import models

class Pagos_repartidor(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('fallido', 'Fallido'),
    ]

    id_pagos = models.AutoField(primary_key=True)
    id_Repartidor = models.IntegerField(db_column='id_Repartidor') 
    monto_total_generado = models.DecimalField(max_digits=12, decimal_places=2)
    comision_plataforma = models.DecimalField(max_digits=12, decimal_places=2)
    monto_neto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )