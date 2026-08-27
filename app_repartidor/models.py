from django.db import models

class Repartidor(models.Model):
    idRepartidor = models.AutoField(primary_key=True)
    Nombres = models.CharField(max_length=100, null=True, blank=True)
    Apellidos = models.CharField(max_length=100, null=True, blank=True)
    Nro_Identificacion = models.CharField(max_length=30, null=True, blank=True)
    Telefono = models.CharField(max_length=20, null=True, blank=True)
    Estado = models.CharField(max_length=50, null=True, blank=True)
    Observacion_Rechazo = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.Nombres} {self.Apellidos}"