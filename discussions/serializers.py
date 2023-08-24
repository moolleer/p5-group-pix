from rest_framework import serializers
from .models import Discussion
from groups.models import Group
from comments.models import Comment
from comments.serializers import CommentSerializer


class DiscussionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Discussion model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    group = serializers.ReadOnlyField(source='group.name')

    created_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S %Z', read_only=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Discussion
        fields = [
            'id', 'group', 'owner', 'title', 'content',
            'created_at', 'is_owner',
        ]


class DiscussionDetailSerializer(DiscussionSerializer):
    """
    Serializer for the DiscussionDetail view
    """
    comments = CommentSerializer(many=True, read_only=True)

    class Meta(DiscussionSerializer.Meta):
        fields = DiscussionSerializer.Meta.fields
