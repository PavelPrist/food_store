from rest_framework import permissions
from users.models import User


class IsAuthorOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_superuser
            or request.user.role == User.ADMIN
            or obj.user == request.user
        )
