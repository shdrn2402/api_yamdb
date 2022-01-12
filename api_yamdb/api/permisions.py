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


class ReviewCommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == self.ROLE_CHOICES.MODERATOR
                or request.user.role == self.ROLE_CHOICES.ADMIN
                or obj.owner == request.user)
