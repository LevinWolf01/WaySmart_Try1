from django.db import models
from django.contrib.auth.models import User

class Empresa(models.Model):
    class TipoColaboracion(models.TextChoices):
        SOCIO = 'SOCIO', 'Socio Comercial'
        PROVEEDOR = 'PROVEEDOR', 'Proveedor'
        ALIADO = 'ALIADO', 'Aliado Estratégico'

    class EstadoEmpresa(models.TextChoices):
        PENDIENTE = 'PENDIENTE', 'Pendiente'
        APROBADO = 'APROBADO', 'Aprobado'
        RECHAZADO = 'RECHAZADO', 'Rechazado'

    idEmpresa = models.BigAutoField(primary_key=True)
    Usuario_idUsuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    Nombre = models.CharField(max_length=200)
    Nit = models.CharField(max_length=50, unique=True)
    Direccion = models.CharField(max_length=300)
    Telefono_contacto = models.CharField(max_length=20)
    Representante_legal_nombre = models.CharField(max_length=200)
    Representante_legal_telefono = models.CharField(max_length=20)
    Representante_legal_correo = models.EmailField(max_length=225)
    Tipo_colaboracion = models.CharField(max_length=50, choices=TipoColaboracion.choices)
    Estado = models.CharField(max_length=50, choices=EstadoEmpresa.choices, default=EstadoEmpresa.PENDIENTE)
    Observacion_rechazo = models.TextField(blank=True, null=True)
    Fecha_validacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.Nombre

class Convenios(models.Model):
    class EstadoConvenio(models.TextChoices):
        ACTIVO = 'ACTIVO', 'Activo'
        INACTIVO = 'INACTIVO', 'Inactivo'
        FINALIZADO = 'FINALIZADO', 'Finalizado'

    convenio_id = models.BigAutoField(primary_key=True)
    Empresa_idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='convenios', verbose_name="Empresa")
    porcentaje_comision = models.DecimalField(max_digits=5, decimal_places=2)
    zonas_cobertura = models.TextField(help_text="Zonas de cobertura")
    condiciones_facturacion = models.TextField()
    fecha_inicion = models.DateField(verbose_name="Fecha de Inicio")
    fecha_termino = models.DateField(verbose_name="Fecha de Término")
    estado = models.CharField(max_length=50, choices=EstadoConvenio.choices, default=EstadoConvenio.ACTIVO)

    def __str__(self):
        return f"Convenio #{self.convenio_id} - {self.Empresa_idEmpresa.Nombre}"