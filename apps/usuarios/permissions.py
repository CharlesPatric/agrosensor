from rest_framework.permissions import BasePermission
from .models import PerfilUsuario

class EsAdministrador(BasePermission):
    """
    Permite el acceso únicamente a usuarios
    con rol ADMIN.
    """

    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        try:
            return request.user.perfil.rol == "ADMIN"
        except AttributeError:
            return False


class EsIngeniero(BasePermission):
    """
    Permite el acceso únicamente a usuarios
    con rol INGENIERO.
    """

    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        try:
            return request.user.perfil.rol == "INGENIERO"
        except AttributeError:
            return False


class EsAgricultor(BasePermission):
    """
    Permite el acceso únicamente a usuarios
    con rol AGRICULTOR.
    """

    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        try:
            return request.user.perfil.rol == "AGRICULTOR"
        except AttributeError:
            return False

class PuedeGestionarEmpresas(BasePermission):
    """
    Controla el acceso a las empresas según
    el método HTTP y el rol del usuario.
    """

    def has_permission(self, request, view):

        if not request.user or not request.user.is_authenticated:
            return False

        try:
            rol = request.user.perfil.rol
        except AttributeError:
            return False

        # Consultas permitidas a todos los usuarios autenticados
        if request.method in ["GET", "HEAD", "OPTIONS"]:
            return True

        # Operaciones de escritura solamente para administradores
        return rol == PerfilUsuario.Rol.ADMIN