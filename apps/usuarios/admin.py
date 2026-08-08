from django.contrib import admin

from .models import PerfilUsuario


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "usuario",
        "empresa",
        "cargo",
        "telefono",
        "activo",
        "fecha_creacion",
    )

    search_fields = (
        "usuario__username",
        "usuario__email",
        "empresa__nombre",
        "cargo",
    )

    list_filter = (
        "activo",
        "empresa",
    )

    ordering = (
        "usuario__username",
    )