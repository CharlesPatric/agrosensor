from django.db import models

from apps.parcelas.models import Parcela


class Dispositivo(models.Model):

    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
        ("MANTENIMIENTO", "Mantenimiento"),
        ("FUERA_SERVICIO", "Fuera de servicio"),
    ]

    parcela = models.ForeignKey(
        Parcela,
        on_delete=models.CASCADE,
        related_name="dispositivos"
    )

    nombre = models.CharField(
        max_length=150
    )

    codigo = models.CharField(
        max_length=50,
        unique=True
    )

    ubicacion = models.CharField(
        max_length=250,
        blank=True
    )

    ip_comunicacion = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    mac_address = models.CharField(
        max_length=17,
        unique=True,
        null=True,
        blank=True
    )

    firmware_version = models.CharField(
        max_length=50,
        blank=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="ACTIVO"
    )

    ultimo_contacto = models.DateTimeField(
        null=True,
        blank=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"