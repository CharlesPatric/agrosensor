from rest_framework import serializers


class MedicionSerializer(serializers.Serializer):

    id = serializers.CharField()

    dispositivoId = serializers.CharField()

    estado = serializers.CharField(
        allow_null=True,
        required=False
    )

    humedadAmbiente = serializers.FloatField(
        allow_null=True,
        required=False
    )

    humedadSuelo = serializers.FloatField(
        allow_null=True,
        required=False
    )

    lugarId = serializers.CharField(
        allow_null=True,
        required=False
    )

    temperatura = serializers.FloatField(
        allow_null=True,
        required=False
    )

    ts = serializers.DateTimeField(
        allow_null=True,
        required=False
    )