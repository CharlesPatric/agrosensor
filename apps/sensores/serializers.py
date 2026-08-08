from rest_framework import serializers

from .models import Sensor


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor

        fields = [
            "id",
            "dispositivo",
            "codigo",
            "nombre",
            "tipo",
            "unidad_medida",
            "estado",
            "fecha_creacion",
        ]

        read_only_fields = [
            "id",
            "fecha_creacion",
        ]