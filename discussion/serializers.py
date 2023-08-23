from rest_framework import serializers
from .models import Discussion, Comment


class DiscussionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Discussion model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S %Z', read_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Discussion
        fields = [
            'id', 'group', 'owner', 'title', 'content',
            'created_at', 'is_owner', 'comments',
        ]
