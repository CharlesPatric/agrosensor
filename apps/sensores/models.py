from django.db import models

from apps.dispositivos.models import Dispositivo


class Sensor(models.Model):

    TIPOS = [
        ("TEMPERATURA", "Temperatura"),
        ("HUMEDAD_SUELO", "Humedad del suelo"),
        ("HUMEDAD_AMBIENTE", "Humedad ambiente"),
        ("PRESION", "Presión atmosférica"),
        ("VIENTO", "Viento"),
    ]

    dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE,
        related_name="sensores"
    )

    nombre = models.CharField(
        max_length=150
    )

    codigo = models.CharField(
        max_length=50,
        unique=True
    )

    tipo = models.CharField(
        max_length=30,
        choices=TIPOS
    )

    unidad_medida = models.CharField(
        max_length=20
    )

    estado = models.BooleanField(
        default=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"