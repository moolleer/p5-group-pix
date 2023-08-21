from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'join_date', 'last_login', 'name',
            'content', 'profile_picture',
        ]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.content = validated_data.get('content', instance.content)
        instance.profile_picture = validated_data.get(
            'profile_picture', instance.profile_picture)
        instance.save()
        return instance
