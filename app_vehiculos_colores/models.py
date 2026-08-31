from django.db import models


class Modelo(models.Model):
    id_modelo = models.AutoField(
        primary_key=True,
        db_column="idModelo"
    )
    nombre = models.CharField(
        max_length=100,
        db_column="Nombre"
    )

    class Meta:
        db_table = "Modelo"
        verbose_name = "Modelo"
        verbose_name_plural = "Modelos"

    def __str__(self):
        return self.nombre


class Repartidor(models.Model):
    id_repartidor = models.BigAutoField(
        primary_key=True,
        db_column="idRepartidor"
    )
    nombre = models.CharField(
        max_length=150,
        db_column="Nombre"
    )

    class Meta:
        db_table = "Repartidor"
        verbose_name = "Repartidor"
        verbose_name_plural = "Repartidores"

    def __str__(self):
        return self.nombre


class Color(models.Model):
    id_colores = models.AutoField(
        primary_key=True,
        db_column="idColores"
    )
    rojo = models.PositiveIntegerField(
        default=0,
        db_column="Rojo"
    )
    amarillo = models.PositiveIntegerField(
        default=0,
        db_column="Amarillo"
    )
    verde = models.PositiveIntegerField(
        default=0,
        db_column="Verde"
    )
    negro = models.PositiveIntegerField(
        default=0,
        db_column="Negro"
    )

    class Meta:
        db_table = "Colores"
        verbose_name = "Color"
        verbose_name_plural = "Colores"
        ordering = ["id_colores"]

    def __str__(self):
        return f"Color {self.id_colores}"


class Vehiculo(models.Model):
    TIPOS = [
        ("MOTO", "Moto"),
        ("CARRO", "Carro"),
        ("CAMIONETA", "Camioneta"),
        ("FURGON", "Furgón"),
        ("OTRO", "Otro"),
    ]

    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
        ("RECHAZADO", "Rechazado"),
        ("PENDIENTE", "Pendiente"),
    ]

    id_vehiculo = models.BigAutoField(
        primary_key=True,
        db_column="idVehiculo"
    )

    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.PROTECT,
        db_column="Modelo_idModelo",
        related_name="vehiculos"
    )

    color = models.ForeignKey(
        Color,
        on_delete=models.PROTECT,
        db_column="Colores_idColores",
        related_name="vehiculos"
    )

    repartidor = models.ForeignKey(
        Repartidor,
        on_delete=models.PROTECT,
        db_column="Repartidor_idRepartidor",
        related_name="vehiculos"
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS,
        db_column="Tipo"
    )

    marca = models.CharField(
        max_length=100,
        db_column="Marca"
    )

    linea = models.CharField(
        max_length=100,
        db_column="Linea"
    )

    placa = models.CharField(
        max_length=20,
        unique=True,
        db_column="Placa"
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        db_column="Estado"
    )

    observacion_rechazo = models.TextField(
        blank=True,
        null=True,
        db_column="Observacion_Rechazo"
    )

    activo = models.BooleanField(
        default=True,
        db_column="Activo"
    )

    fecha_validacion = models.DateTimeField(
        null=True,
        blank=True,
        db_column="Fecha_Validacion"
    )

    class Meta:
        db_table = "Vehiculo"
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"
        ordering = ["-id_vehiculo"]

    def __str__(self):
        return f"{self.placa} - {self.marca}"
