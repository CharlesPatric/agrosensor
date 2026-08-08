from rest_framework import serializers

from .models import Dispositivo


class DispositivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dispositivo

        fields = [
            "id",
            "nombre",
            "codigo",
            "parcela",
            "ubicacion",
            "ip_comunicacion",
            "mac_address",
            "firmware_version",
            "estado",
            "ultimo_contacto",
            "fecha_creacion",
        ]

        read_only_fields = [
            "id",
            "fecha_creacion",
            "ultimo_contacto",
        ]