
from django.db import models

# Create your models here.



class Empresa(models.Model):
    nombre = models.CharField(
        max_length=150,
        verbose_name="Nombre"
    )

    nit = models.CharField(
        max_length=30,
        unique=True,
        verbose_name="NIT"
    )

    direccion = models.CharField(
        max_length=250,
        blank=True
    )

    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    correo = models.EmailField(
        blank=True
    )

    activa = models.BooleanField(
        default=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre