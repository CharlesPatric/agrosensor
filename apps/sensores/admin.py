from django.contrib import admin

from .models import Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "codigo",
        "nombre",
        "dispositivo",
        "tipo",
        "unidad_medida",
        "estado",
        "fecha_creacion",
    )

    search_fields = (
        "codigo",
        "nombre",
        "dispositivo__codigo",
    )

    list_filter = (
        "tipo",
        "estado",
    )

    ordering = (
        "codigo",
    )