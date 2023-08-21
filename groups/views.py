from rest_framework import generics, permissions
from .models import Group
from .serializers import GroupSerializer, GroupDetailSerializer
from group_pix.permissions import IsGroupOwnerOrReadOnly


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
    queryset = Group.objects.all()
    serializer_class = GroupDetailSerializer
    permission_classes = [permissions.IsAuthenticated, IsGroupOwnerOrReadOnly]
