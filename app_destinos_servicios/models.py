from django.db import models


class Servicio(models.Model):
	ESTADOS = [
		('Solicitado', 'Solicitado'),
		('En Proceso', 'En Proceso'),
		('Completado', 'Completado'),
		('Cancelado', 'Cancelado'),
	]

	empresa_id          = models.BigIntegerField()
	codigo_servicio     = models.CharField(max_length=50)
	tipo_envio          = models.CharField(max_length=100, blank=True)
	cantidad_entregas   = models.PositiveIntegerField(null=True, blank=True)
	direccion_recogidas = models.CharField(max_length=500)
	fecha_deseada       = models.DateTimeField(null=True, blank=True)
	estado              = models.CharField(max_length=20, choices=ESTADOS, default='Solicitado')
	observaciones       = models.TextField(blank=True)

	def __str__(self):
		return self.codigo_servicio


class Destino(models.Model):
	PRIORIDADES = [
		('Baja', 'Baja'),
		('Media', 'Media'),
		('Alta', 'Alta'),
	]
	ESTADOS_ENTREGA = [
		('Pendiente', 'Pendiente'),
		('En Ruta', 'En Ruta'),
		('Entregado', 'Entregado'),
		('Cancelado', 'Cancelado'),
	]

	id_pago_entrega         = models.BigIntegerField(null=True, blank=True)
	servicio_id             = models.BigIntegerField(null=True, blank=True)
	asignacion_id           = models.BigIntegerField(null=True, blank=True)
	nombre_destinatario     = models.CharField(max_length=150)
	telefono_destinatario   = models.CharField(max_length=30, blank=True)
	direccion               = models.CharField(max_length=500)
	latitud                 = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
	longitud                = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
	prioridad               = models.CharField(max_length=10, choices=PRIORIDADES, default='Media')
	estado_entrega          = models.CharField(max_length=20, choices=ESTADOS_ENTREGA, default='Pendiente')
	firma_digital_url       = models.URLField(max_length=500, blank=True)
	fecha_entrega           = models.DateTimeField(null=True, blank=True)
	observaciones           = models.TextField(blank=True)

	def __str__(self):
		return self.nombre_destinatario
