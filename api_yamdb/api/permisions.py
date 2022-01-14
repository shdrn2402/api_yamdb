from rest_framework import permissions


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
                and request.user.role == self.ROLE_CHOICES.ADMIN)
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user.is_authenticated
                and request.user.role == self.ROLE_CHOICES.ADMIN)
        )


class IsSuperuser(permissions.BasePermission):
    pass
