"""Create custom permission for accessing the api"""

from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile data"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        """this will return true false and only the user can modify his details"""
        return obj.id == request.user.id