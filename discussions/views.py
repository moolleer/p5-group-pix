from rest_framework import generics, permissions
from group_pix.permissions import (
    IsGroupMemberDiscussion,
    IsOwnerOrReadOnly,
    IsGroupCreatorDiscussion,
    IsGroupMemberOrCreator
    )
from rest_framework.response import Response
from .models import Discussion
from groups.models import Group
from comments.serializers import CommentDiscussionDetailSerializer
from .serializers import DiscussionSerializer


class DiscussionListCreateView(generics.ListCreateAPIView):
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticated, IsGroupMemberOrCreator]

    def get_queryset(self):
        group_pk = self.kwargs['pk']
        return Discussion.objects.filter(group__pk=group_pk)

    def perform_create(self, serializer):
        group_pk = self.kwargs['pk']
        group = Group.objects.get(pk=group_pk)
        serializer.save(owner=self.request.user, group=group)


class DiscussionDetailView(generics.RetrieveAPIView):
    serializer_class = DiscussionSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsGroupCreatorDiscussion,
        IsGroupMemberDiscussion
    ]

    def get_queryset(self):
        group_pk = self.kwargs['group_pk']
        return Discussion.objects.filter(
            group__pk=group_pk).prefetch_related('comments')


class DiscussionDetailOwner(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscussionSerializer
    permission_classes = [
        permissions.IsAuthenticated, IsOwnerOrReadOnly
    ]
    queryset = Discussion.objects.all()
    lookup_url_kwarg = 'discussion_pk'
