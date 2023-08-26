from django.db.models import Q
from django.shortcuts import Http404
from rest_framework import generics, permissions
from .models import Comment
from discussions.models import Discussion
from posts.models import Post
from .serializers import (
    CommentSerializer,
    CommentDiscussionDetailSerializer,
    CommentPostDetailSerializer
)
from group_pix.permissions import (
    IsGroupMemberOrCreatorPostOrDiscussion,
    IsOwnerOrReadOnly
)


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsGroupMemberOrCreatorPostOrDiscussion
    ]

    def get_queryset(self):
        group_pk = self.kwargs['group_pk']
        queryset = Comment.objects.filter(
            Q(post__group__pk=group_pk) | Q(discussion__group__pk=group_pk)
        )
        if 'post_pk' in self.kwargs:
            queryset = queryset.filter(post__pk=self.kwargs['post_pk'])
        elif 'discussion_pk' in self.kwargs:
            queryset = queryset.filter(
                discussion__pk=self.kwargs['discussion_pk'])
        return queryset

    def perform_create(self, serializer):
        group_pk = self.kwargs['group_pk']

        if 'post_pk' in self.kwargs:
            # Comment for a post
            post_pk = self.kwargs['post_pk']
            post = Post.objects.get(pk=post_pk, group__pk=group_pk)
            serializer.save(owner=self.request.user, post=post)
        elif 'discussion_pk' in self.kwargs:
            # Comment for a discussion
            discussion_pk = self.kwargs['discussion_pk']
            discussion = Discussion.objects.get(
                pk=discussion_pk, group__pk=group_pk)
            serializer.save(owner=self.request.user, discussion=discussion)


class CommentDetailDiscussion(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [
        permissions.IsAuthenticated, IsGroupMemberOrCreatorPostOrDiscussion
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentDiscussionDetailSerializer


class CommentDetailPost(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAuthenticated, IsGroupMemberOrCreatorPostOrDiscussion
    ]
    queryset = Comment.objects.all()
    serializer_class = CommentPostDetailSerializer
