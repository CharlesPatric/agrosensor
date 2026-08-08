from django.contrib import admin

from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nombre",
        "nit",
        "telefono",
        "activa",
        "fecha_creacion",
    )

    search_fields = (
        "nombre",
        "nit",
    )

    list_filter = (
        "activa",
    )

    ordering = (
        "nombre",
    )