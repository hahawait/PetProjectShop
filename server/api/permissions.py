from rest_framework.permissions import BasePermission, SAFE_METHODS


class AdminOrStafOrReadOnly(BasePermission):
    """
    Класс для проверки прав доступа на основе роли пользователя.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            # Администратор и сотрудник имеет полный доступ
            return True
        else:
            # Другие пользователи имеют доступ только на чтение
            return request.method in SAFE_METHODS


class OwnerOnly(BasePermission):
    """
    Класс для проверки прав доступа только для создателя объекта.
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user