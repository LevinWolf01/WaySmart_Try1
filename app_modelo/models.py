from django.db import models

class Modelo(models.Model):
    idModelo = models.AutoField(primary_key=True)  
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
        return f"Modelo {self.idModelo}"