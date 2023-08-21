from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from group_pix.permissions import IsOwnerOrReadOnly


class ProfileList(APIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer

    def get_object(self):
        try:
            return self.queryset.get(pk=self.kwargs['pk'])
        except Profile.DoesNotExist:
            raise Http404("Profile does not exist")

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        user = instance.owner  
        self.perform_destroy(instance)
        user.delete() 
        return Response({"message": "User and profile successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
