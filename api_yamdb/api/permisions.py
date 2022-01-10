from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )


class IsModerator(permissions.BasePermission):
    
    pass


class IsAdmin(permissions.BasePermission):
    pass


class IsAdminOrReadOnly(permissions.BasePermission):
    pass


class IsSuperuser(permissions.BasePermission):
    pass
