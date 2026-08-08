from rest_framework import serializers

from .models import Parcela


class ParcelaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parcela

        fields = [
            "id",
            "nombre",
            "empresa",
        ]

        read_only_fields = [
            "id",
        ]