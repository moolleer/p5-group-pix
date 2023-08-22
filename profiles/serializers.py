from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.

    This serializer converts Profile model instances into JSON representation
    and handles validation and data updating.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    join_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S %Z')
    last_login = serializers.SerializerMethodField()

    def get_last_login(self, obj):
        return naturaltime(obj.last_login)

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
