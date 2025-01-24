from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверка, является ли пользователь владельцем"""

    def has_object_permission(self, request, view, obj):
        # Сначала проверяем, авторизован ли пользователь
        if not request.user.is_authenticated:
            return False
        return obj.owner == request.user


class IsModer(BasePermission):
    """Проверяет, является ли пользователь модератором"""

    def has_permission(self, request, view):
        # Сначала проверяем, авторизован ли пользователь
        if not request.user.is_authenticated:
            return False
        return request.user.groups.filter(name="moder").exists()
