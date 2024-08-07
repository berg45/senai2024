from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Permissão de leitura são permitidas para qualquer requisição,
        # então sempre permitimos solicitações GET, HEAD ou OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Escreve permissões são permitidas apenas para o dono do objeto.
        return obj.owner == request.user