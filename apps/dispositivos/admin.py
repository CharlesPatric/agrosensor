from django.contrib import admin

from .models import Dispositivo


@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "codigo",
        "nombre",
        "parcela",
        "estado",
        "ip_comunicacion",
        "ultimo_contacto",
        "fecha_creacion",
    )

    search_fields = (
        "codigo",
        "nombre",
        "parcela__nombre",
    )

    list_filter = (
        "estado",
    )

    ordering = (
        "codigo",
    )