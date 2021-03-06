from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self,request,view, obj):
        """Check that the user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnBook(permissions.BasePermission):
    """Allow users to update their own books"""
    def has_object_permission(self, request,view, obj):
        """Check the user is trying to update their own book"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner.id == request.user.id
