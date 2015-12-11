"""
"""
SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
from rest_framework import permissions
from fsop.apps.fsopuser.models import FSOPUser as User


class IsProjectOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an project to edit it.
    """
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == 'POST':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_staff:
            return True
        elif request.user.id == obj.created_by_id:
            return True
        return False
