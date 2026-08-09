from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.dispositivos.models import Dispositivo

from services.firebase.mediciones import obtener_mediciones

from .serializers import MedicionSerializer


class MedicionListAPIView(APIView):

    def get(self, request):

        try:

            dispositivo_id = request.query_params.get(
                "dispositivo"
            )

            firebase_id = None

            if dispositivo_id:

                dispositivo = Dispositivo.objects.get(
                    id=dispositivo_id
                )

                firebase_id = dispositivo.firebase_id

            mediciones = obtener_mediciones(
                firebase_id=firebase_id
            )

            serializer = MedicionSerializer(
                mediciones,
                many=True
            )

            return Response(
                serializer.data
            )

        except Dispositivo.DoesNotExist:

            return Response(
                {
                    "error": "El dispositivo no existe."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception:

            return Response(
                {
                    "error": "No se pudieron obtener las mediciones."
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )