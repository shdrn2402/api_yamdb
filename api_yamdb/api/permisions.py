from rest_framework import permissions
from reviews.models import User


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user # нужно прописать поле author в моделях
            or request.method in permissions.SAFE_METHODS
        )


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.MODERATOR
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.user.role == User.MODERATOR
        )
        

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ADMIN
            or request.user.is_superuser
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.user.role == User.ADMIN 
            or request.user.is_superuser
        )


class IsSuperuser(permissions.BasePermission):
    pass
