from rest_framework import permissions
from groups.models import GroupMembership, Group


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsGroupOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user


class IsGroupMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsGroupCreator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user


class IsGroupMemberOrCreator(permissions.BasePermission):
    """
    Custom permission to allow only group members
    or group creators to create posts.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the user is a member of the group or a group creator
        group_pk = view.kwargs['pk']
        group = Group.objects.get(pk=group_pk)
        return GroupMembership.objects.filter(
            user=request.user, group=group).exists() or \
            request.user == group.created_by
