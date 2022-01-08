from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    pass


class IsModerator(permissions.BasePermission):
    pass


class IsAdmin(permissions.BasePermission):
    pass


class IsAdminOrReadOnly(permissions.BasePermission):
    pass


class IsSuperuser(permissions.BasePermission):
    pass
