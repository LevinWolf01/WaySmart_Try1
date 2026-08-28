from django.db import models

class Modelo(models.Model):
    idModelo = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=100, null=True, blank=True)
    Nombre_Modelo = models.CharField(max_length=100, null=True, blank=True)
    Color = models.CharField(max_length=100, null=True, blank=True)
    Año = models.CharField(max_length=20, null=True, blank=True)
    Placa = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.Marca} {self.Nombre_Modelo}"