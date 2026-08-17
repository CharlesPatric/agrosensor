from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Parcela
from .serializers import ParcelaSerializer
from apps.usuarios.models import PerfilUsuario


class ParcelaViewSet(viewsets.ModelViewSet):

    #queryset = Parcela.objects.all()

    serializer_class = ParcelaSerializer
    
    def get_queryset(self):

        usuario = self.request.user

        if usuario.perfil.rol == PerfilUsuario.Rol.ADMIN:
            return Parcela.objects.all()

        return Parcela.objects.filter(
            empresa=usuario.perfil.empresa
        )