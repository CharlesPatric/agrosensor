from rest_framework import viewsets

from .models import Empresa
from .serializers import EmpresaSerializer
from rest_framework.permissions import IsAuthenticated
from apps.usuarios.permissions import PuedeGestionarEmpresas
#  para usar el perfil de usuario 
from apps.usuarios.models import PerfilUsuario



class EmpresaViewSet(viewsets.ModelViewSet):

   # queryset = Empresa.objects.all()

    serializer_class = EmpresaSerializer
    
    permission_classes = [PuedeGestionarEmpresas]
    
    def get_queryset(self):

        usuario = self.request.user

        # Administrador puede ver todas las empresas
        if usuario.perfil.rol == PerfilUsuario.Rol.ADMIN:
            return Empresa.objects.all()

        # Usuarios normales solamente ven su empresa
        return Empresa.objects.filter(
            id=usuario.perfil.empresa.id
        )