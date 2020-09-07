from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: # любой может выполнять только 'GET', 'HEAD', 'OPTIONS', авторизованный любой
            return True
        return obj.user == request.user