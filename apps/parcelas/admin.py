from django.contrib import admin

from .models import Parcela


@admin.register(Parcela)
class ParcelaAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "nombre",
        "empresa",
        "cultivo",
        "superficie",
        "activa",
        "fecha_creacion",
    )

    search_fields = (
        "nombre",
        "empresa__nombre",
        "cultivo",
    )

    list_filter = (
        "activa",
        "cultivo",
    )

    ordering = (
        "nombre",
    )