from django.db import models

class Repartidor(models.Model):
    # Sin PK (idRepartidor) y sin FK (Usuario_idUsuario)
    Nombres = models.CharField(max_length=255, null=True, blank=True)
    Apellidos = models.CharField(max_length=255, null=True, blank=True)
    Nro_Identificacion = models.CharField(max_length=255, null=True, blank=True)
    Telefono = models.CharField(max_length=20, null=True, blank=True)
    Observacion_Rechazo = models.TextField(null=True, blank=True)
    Fecha_Validacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.Nombres} {self.Apellidos}"

class Modelo(models.Model):
    # Sin PK (idModelo). 
    # En el XML los campos son años (2000, 2001...). En Python no pueden empezar con números, 
    # así que les ponemos "anio_" adelante.
    anio_2000 = models.IntegerField(null=True, blank=True)
    anio_2001 = models.IntegerField(null=True, blank=True)
    anio_2002 = models.IntegerField(null=True, blank=True)
    anio_2003 = models.IntegerField(null=True, blank=True)
    anio_2004 = models.IntegerField(null=True, blank=True)
    anio_2005 = models.IntegerField(null=True, blank=True)
    anio_2006 = models.IntegerField(null=True, blank=True)
    anio_2007 = models.IntegerField(null=True, blank=True)
    anio_2008 = models.IntegerField(null=True, blank=True)
    anio_2009 = models.IntegerField(null=True, blank=True)
    anio_2010 = models.IntegerField(null=True, blank=True)
    anio_2011 = models.IntegerField(null=True, blank=True)
    anio_2012 = models.IntegerField(null=True, blank=True)
    anio_2013 = models.IntegerField(null=True, blank=True)
    anio_2014 = models.IntegerField(null=True, blank=True)
    anio_2015 = models.IntegerField(null=True, blank=True)
    anio_2016 = models.IntegerField(null=True, blank=True)
    anio_2017 = models.IntegerField(null=True, blank=True)
    anio_2018 = models.IntegerField(null=True, blank=True)
    anio_2019 = models.IntegerField(null=True, blank=True)
    anio_2020 = models.IntegerField(null=True, blank=True)
    anio_2021 = models.IntegerField(null=True, blank=True)
    anio_2022 = models.IntegerField(null=True, blank=True)
    anio_2023 = models.IntegerField(null=True, blank=True)
    anio_2024 = models.IntegerField(null=True, blank=True)
    anio_2025 = models.IntegerField(null=True, blank=True)
    anio_2026 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Modelo {self.id}"