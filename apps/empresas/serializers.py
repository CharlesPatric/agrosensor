from rest_framework import serializers

from .models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa

        fields = [
            "id",
            "nombre",
            "nit",
            "direccion",
            "telefono",
            "correo",
            "activa",
            "fecha_creacion",
        ]

        read_only_fields = [
            "id",
            "fecha_creacion",
        ]