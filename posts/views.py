from rest_framework import generics, permissions, serializers, status, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PostSerializer
from .models import Post
from groups.models import Group, GroupMembership
from group_pix.permissions import (
    IsOwnerOrReadOnly,
    IsGroupMember,
    IsGroupCreator,
    IsGroupMemberOrCreator)


class PostCreate(generics.CreateAPIView):
    """
    View for creating a post in a group if you are
    a group member or group creator.
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsGroupMemberOrCreator
    ]

    def get(self, request, *args, **kwargs):
        group = Group.objects.get(pk=self.kwargs['pk'])
        membership = group.members.filter(pk=request.user.pk).exists()

        if membership or group.created_by == request.user:
            message = (
                "You are authorized to create a post in this group."
            )
            return Response(
                {'message': message},
                status=status.HTTP_200_OK
            )
        else:
            message = (
                "You are not authorized to create a post in this group."
            )
            return Response(
                {'message': message},
                status=status.HTTP_403_FORBIDDEN
            )

    def perform_create(self, serializer):
        group_pk = self.kwargs['pk']
        group = Group.objects.get(pk=group_pk)

        serializer.save(owner=self.request.user, group=group)


class PostList(generics.ListAPIView):
    """
    View for listing posts in a group
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        group_pk = self.kwargs['pk']
        return Post.objects.filter(group__pk=group_pk)

    filter_backends = [
        DjangoFilterBackend, filters.SearchFilter
    ]
    filterset_fields = ['owner__profile']
    search_fields = ['owner__username', 'title', 'content']


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post if a user is logged in, edit or delete
    it if the user owns it.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
