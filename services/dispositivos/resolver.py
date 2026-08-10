from apps.dispositivos.models import Dispositivo
from apps.parcelas.models import Parcela


def obtener_dispositivo_por_firebase_id(firebase_id):

    try:
        return Dispositivo.objects.select_related(
            "parcela"
        ).get(
            firebase_id=firebase_id
        )

    except Dispositivo.DoesNotExist:
        return None


def obtener_parcela_por_firebase_id(firebase_id):

    try:
        return Parcela.objects.get(
            firebase_id=firebase_id
        )

    except Parcela.DoesNotExist:
        return None