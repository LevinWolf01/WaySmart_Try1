from django.db import models

# Create your models here.
class Seguimiento_Geolocalizacion(models.Model):
    id_Seguimiento = models.AutoField(primary_key=True)
    id_Repartidor = models.IntegerField(db_column='id_Repartidor') 
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)
    velocidad = models.IntegerField()