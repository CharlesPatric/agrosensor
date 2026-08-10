from rest_framework import serializers

from .models import Parcela
from apps.empresas.models import Empresa

class EmpresaResumenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa

        fields = [
            "id",
            "nombre",
        ]

class ParcelaSerializer(serializers.ModelSerializer):

    empresa = EmpresaResumenSerializer(read_only=True)
    empresa_id = serializers.PrimaryKeyRelatedField(
        queryset=Empresa.objects.all(),
        source="empresa",
        write_only=True
    )
    class Meta:
        model = Parcela

        fields = [
            "id",
            "nombre",
            "empresa",
            "empresa_id",
            "firebase_id",
        ]

        read_only_fields = [
            "id",
        ]


