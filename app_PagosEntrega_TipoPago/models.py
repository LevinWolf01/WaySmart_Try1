from django.db import models

class TipoDePago(models.Model):
    id_tipo_de_pago = models.AutoField(primary_key=True, db_column='idTipo de Pago')
    efectivo = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, db_column='Efectivo')
    transferencia = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, db_column='Transferencia')

    class Meta:
        db_table = 'Tipo de Pago'

    def __str__(self):
        return f"Tipo Pago #{self.id_tipo_de_pago}"


class PagosEntrega(models.Model):
    METODO_CHOICES = [
        ('EFECTIVO', 'Efectivo'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('OTRO', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADO', 'Completado'),
        ('CANCELADO', 'Cancelado'),
    ]

    id_pago_entrega = models.BigAutoField(primary_key=True, db_column='idPago Entrega')
    tipo_de_pago = models.ForeignKey(
        TipoDePago, 
        on_delete=models.CASCADE, 
        db_column='Tipo de Pago_idTipo de Pago'
    )
    valor_total = models.DecimalField(max_digits=12, decimal_places=2, db_column='Valor Total')
    metodo_pago = models.CharField(max_length=50, choices=METODO_CHOICES, db_column='Metodo Pago')
    evidencia_url = models.CharField(max_length=255, null=True, blank=True, db_column='Evidencia Url')
    fecha_de_pago = models.DateTimeField(db_column='Fecha De Pago')
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, db_column='Estado')

    class Meta:
        db_table = 'Pagos Entrega'

    def __str__(self):
        return f"Pago #{self.id_pago_entrega} - {self.estado}"