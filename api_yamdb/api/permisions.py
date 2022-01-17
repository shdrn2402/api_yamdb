from rest_framework import permissions
from reviews.models import User


class IsAuthor(permissions.BasePermission):
    pass


class IsModerator(permissions.BasePermission):
    pass


class IsAdmin(permissions.BasePermission):
    pass


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and request.user.role == User.ADMIN)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and request.user.role == User.ADMIN)
        )


class ReviewCommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == User.MODERATOR
                or request.user.role == User.ADMIN
                or obj.owner == request.user)
