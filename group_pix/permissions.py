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


class IsGroupMemberDiscussion(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        group_pk = view.kwargs['group_pk']
        group = Group.objects.get(pk=group_pk)
        return group.members.filter(pk=request.user.pk).exists()


class IsGroupCreatorDiscussion(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        group_pk = view.kwargs['group_pk']
        group = Group.objects.get(pk=group_pk)
        return group.created_by == request.user


class IsGroupMemberOrCreator(permissions.BasePermission):
    """
    Custom permission to allow only group members
    or group creators to create posts.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        group_pk = view.kwargs['pk']
        group = Group.objects.get(pk=group_pk)
        return GroupMembership.objects.filter(
            user=request.user, group=group).exists() or \
            request.user == group.created_by


class IsGroupMemberOrCreatorPostOrDiscussion(permissions.BasePermission):
    """
    Custom permission to allow only group members
    or group creators to interact with discussions and posts.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Get the group from the URL parameters
        group_pk = view.kwargs.get('group_pk')

        # Check if the user is a member of the group or a group creator
        return GroupMembership.objects.filter(
            user=request.user, group__pk=group_pk).exists() or \
            request.user == Group.objects.get(pk=group_pk).created_by
