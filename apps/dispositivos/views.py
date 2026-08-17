from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Dispositivo
from .serializers import DispositivoSerializer
from apps.usuarios.models import PerfilUsuario

class DispositivoViewSet(viewsets.ModelViewSet):

    #queryset = Dispositivo.objects.all()

    serializer_class = DispositivoSerializer
    def get_queryset(self):

        usuario = self.request.user

        if usuario.perfil.rol == PerfilUsuario.Rol.ADMIN:
            return Dispositivo.objects.all()

        return Dispositivo.objects.filter(
            parcela__empresa=usuario.perfil.empresa
        )