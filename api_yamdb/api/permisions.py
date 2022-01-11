from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user # нужно прописть поле author в моделях
            or request.method in permissions.SAFE_METHODS
        )


class IsModerator(permissions.BasePermission): # не уверен, что работает. Нужно тестить

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == self.ROLE_CHOICES.MODERATOR
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.user.role == self.ROLE_CHOICES.MODERATOR
        )
        


class IsAdmin(permissions.BasePermission): # не уверен, что работает. Нужно тестить

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == self.ROLE_CHOICES.ADMIN
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated
            and request.user.role == self.ROLE_CHOICES.ADMIN 
        )


class IsSuperuser(permissions.BasePermission):
    pass
