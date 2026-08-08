
# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from apps.empresas.models import Empresa


class PerfilUsuario(models.Model):

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil"
    )

    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        related_name="usuarios"
    )

    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    cargo = models.CharField(
        max_length=100,
        blank=True
    )

    activo = models.BooleanField(
        default=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.usuario.username