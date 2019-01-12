from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return request.user.is_staff
        else:
            if request.method == 'GET':
                return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return request.user.is_staff
        else:
            if request.method == 'GET':
                return True
