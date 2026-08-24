from django.db import models

class Repartidor(models.Model):
    idRepartidor = models.AutoField(primary_key=True)  # <--- PK AGREGADA
    # Usuario_idUsuario (Lo dejamos comentado porque la tabla Usuario aún no existe en tu app)
    # Pero cuando la agreguen, aquí se pondrá: usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)

    Nombres = models.CharField(max_length=255, null=True, blank=True)
    Apellidos = models.CharField(max_length=255, null=True, blank=True)
    Nro_Identificacion = models.CharField(max_length=255, null=True, blank=True)
    Telefono = models.CharField(max_length=20, null=True, blank=True)
    Observacion_Rechazo = models.TextField(null=True, blank=True)
    Fecha_Validacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.Nombres} {self.Apellidos}"