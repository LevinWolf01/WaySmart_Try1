from django.db import models

# Create your models here.

class Usuario(models.Model):
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    rol = models.CharField(max_length=50, choices=[('admin','Admin'),('cliente','Cliente'),('repartidor','Repartidor')])
    estado = models.CharField(max_length=20, choices=[('activo','Activo'),('inactivo','Inactivo')])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Documento(models.Model):
    tipo_documento = models.CharField(max_length=100)
    url_archivo = models.CharField(max_length=200)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('vigente','Vigente'),('expirado','Expirado')])

    # Relaciones
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    empresa_id = models.BigIntegerField(null=True, blank=True)
    repartidor_id = models.BigIntegerField(null=True, blank=True)
    entidad_tipo = models.CharField(max_length=50, choices=[('empresa','Empresa'),('repartidor','Repartidor')])
    entidad_id = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.tipo_documento
