from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group, GroupMembership
from .serializers import (
    GroupSerializer,
    GroupDetailSerializer,
    GroupMembershipSerializer)
from group_pix.permissions import IsGroupOwnerOrReadOnly, IsGroupMember


class GroupList(generics.ListCreateAPIView):
    """
    List all groups
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a specific group.
    Only the group owner can perform update and delete actions.
    """
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsGroupOwnerOrReadOnly]


class GroupMembershipList(generics.ListAPIView):
    """
    List all group memberships of the requesting user
    """
    serializer_class = GroupMembershipSerializer
    permission_classes = [permissions.IsAuthenticated, IsGroupMember]

    def get_queryset(self):
        """
        Return a queryset of group memberships belonging
        to the requesting user.
        """
        user = self.request.user
        return GroupMembership.objects.filter(user=user)


class GroupJoinView(generics.CreateAPIView):
    """
    Join a group or check if the requesting user is already a member.
    """
    serializer_class = GroupMembershipSerializer
    permission_classes = [permissions.IsAuthenticated, IsGroupMember]

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=self.kwargs['pk'])
        membership = GroupMembership.objects.filter(
            user=request.user, group=group).exists()

        if membership:
            return Response(
                {'message': 'You are already a member of this group.'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'message': 'You are not a member of this group yet.'},
            status=status.HTTP_404_NOT_FOUND
        )

    def create(self, request, *args, **kwargs):
        group = Group.objects.get(pk=self.kwargs['pk'])
        membership, created = GroupMembership.objects.get_or_create(
            user=request.user, group=group)
        if created:
            return Response(
                {'message': 'You have joined the group.'},
                status=status.HTTP_201_CREATED)
        return Response(
            {'message': 'You are already a member of this group.'},
            status=status.HTTP_400_BAD_REQUEST)


class GroupMembershipLeave(APIView):
    """
    Leave a group or check membership status and group details.
    """
    permission_classes = [permissions.IsAuthenticated, IsGroupMember]

    def get(self, request, pk, format=None):
        try:
            group = Group.objects.get(id=pk)
            membership = GroupMembership.objects.get(
                user=request.user, group=group)

            if group.created_by == request.user:
                message = (
                    "As the group creator, you are automatically a "
                    "member of this group."
                )
                return Response(
                    {"message": message},
                    status=status.HTTP_200_OK
                )
            serializer = GroupMembershipSerializer(membership)
            return Response(serializer.data)
        except Group.DoesNotExist:
            return Response(
                {"message": "Group not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except GroupMembership.DoesNotExist:
            return Response(
                {"message": "You are not a member of this group."},
                status=status.HTTP_403_FORBIDDEN
            )

    def delete(self, request, pk, format=None):
        try:
            group = Group.objects.get(id=pk)
            membership = GroupMembership.objects.get(
                user=request.user, group=group)

            if group.created_by == request.user:
                return Response(
                    {"message": "Group creator cannot leave the group."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            membership.delete()
            return Response({"message": "You have left the group."},
                            status=status.HTTP_204_NO_CONTENT)
        except GroupMembership.DoesNotExist:
            message = (
                "You are not a member of this"
                "group so you cant leave the group."
            )
            return Response({"message": message},
                            status=status.HTTP_400_BAD_REQUEST)
