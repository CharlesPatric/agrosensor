from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.dispositivos.models import Dispositivo

from services.firebase.mediciones import obtener_mediciones

from .serializers import MedicionSerializer
from .transformers import enriquecer_medicion

class MedicionListAPIView(APIView):

    def get(self, request):

        try:

            dispositivo_id = request.query_params.get(
                "dispositivo"
            )

            firebase_id = None

            #if dispositivo_id:

             #   dispositivo = Dispositivo.objects.get(
              #      id=dispositivo_id
                #)

              #  firebase_id = dispositivo.firebase_id
            if dispositivo_id:

                dispositivo = Dispositivo.objects.get(
                    id=dispositivo_id,
                    parcela__empresa=request.user.perfil.empresa
                )

                firebase_id = dispositivo.firebase_id

            mediciones = obtener_mediciones(
                firebase_id=firebase_id
            )

            serializer = MedicionSerializer(
                mediciones,
                many=True
            )
            mediciones_enriquecidas = [
            enriquecer_medicion(medicion)
            for medicion in mediciones
            ]

            return Response(mediciones_enriquecidas)    
            

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