from rest_framework import serializers
from .models import Group, GroupMembership


class GroupSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Group
        fields = [
            'id', 'name', 'description',
            'created_by', 'created_at',
        ]


class GroupDetailSerializer(GroupSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta(GroupSerializer.Meta):
        fields = GroupSerializer.Meta.fields + ['members']


class GroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembership
        fields = ['user', 'group', 'joined_at']
