from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    group = serializers.ReadOnlyField(source='group.name')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S %Z', read_only=True)
    updated_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S %Z', read_only=True)
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'group', 'title',
            'content', 'image', 'created_at', 'updated_at',
            'profile_image', 'is_owner',
        ]
