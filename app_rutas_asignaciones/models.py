from django.db import models

# Create your models here.

class Asignacion(models.Model):
    asignacion_id = models.BigAutoField(primary_key=True)
    servicios_servicios_id = models.BigIntegerField()
    servicio_id = models.BigIntegerField()
    repartidor_id = models.BigIntegerField()
    fecha_aceptacion = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=50)

    class Meta:
        db_table = 'asignaciones'

    def __str__(self):
        return f'Asignación {self.asignacion_id}'


class Ruta(models.Model):
    idrutas = models.BigAutoField(primary_key=True)
    asignacion = models.ForeignKey(
        Asignacion,
        on_delete=models.CASCADE,
        db_column='Asignaciones_asignacion_id'
    )
    tipo_ruta = models.CharField(max_length=50)
    tiempo_estimado_min = models.IntegerField()
    polyline_json = models.TextField()
    seleccionada = models.BooleanField(default=False)

    class Meta:
        db_table = 'rutas'

    def __str__(self):
        return f'Ruta {self.idrutas}'
