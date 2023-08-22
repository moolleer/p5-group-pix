from rest_framework import serializers
from .models import Group, GroupMembership


class GroupSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S %Z')

    class Meta:
        model = Group
        fields = [
            'id', 'name', 'description',
            'created_by', 'created_at',
        ]


class GroupDetailSerializer(GroupSerializer):
    members = serializers.SerializerMethodField()

    class Meta(GroupSerializer.Meta):
        fields = GroupSerializer.Meta.fields + ['members']

    def get_members(self, obj):
        return [member.username for member in obj.members.all()]


class GroupMembershipSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    group = serializers.ReadOnlyField(source='group.name')
    joined_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S %Z')

    class Meta:
        model = GroupMembership
        fields = ['id', 'user', 'group', 'joined_at']
