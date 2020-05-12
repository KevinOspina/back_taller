from rest_framework.permissions import IsAuthenticated, BasePermission


class Allow(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
