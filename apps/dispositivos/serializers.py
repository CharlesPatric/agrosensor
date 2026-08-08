from rest_framework import serializers
from apps.parcelas.models import Parcela
from .models import Dispositivo

class ParcelaResumenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parcela

        fields = [
            "id",
            "nombre",
        ]
        
class DispositivoSerializer(serializers.ModelSerializer):

    parcela = ParcelaResumenSerializer(read_only=True)

    parcela_id = serializers.PrimaryKeyRelatedField(
        queryset=Parcela.objects.all(),
        source="parcela",
        write_only=True
    )

    class Meta:
        model = Dispositivo

        fields = [
            "id",
            "nombre",
            "codigo",
            "firebase_id",
            "parcela",
            "parcela_id",
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