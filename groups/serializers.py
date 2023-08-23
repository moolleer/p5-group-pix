from rest_framework import serializers
from .models import Group, GroupMembership


class GroupSerializer(serializers.ModelSerializer):
    """
    Serializer for the Group model.
    """
    created_by = serializers.ReadOnlyField(source='created_by.username')
    created_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S %Z', read_only=True)
    is_creator = serializers.SerializerMethodField()
    is_member = serializers.SerializerMethodField()

    def get_is_creator(self, obj):
        request = self.context['request']
        return request.user == obj.created_by

    def get_is_member(self, obj):
        request = self.context['request']
        return obj.members.filter(id=request.user.id).exists()

    class Meta:
        model = Group
        fields = [
            'id', 'name', 'description',
            'created_by', 'created_at', 'is_creator',
            'is_member',
        ]


class GroupDetailSerializer(GroupSerializer):
    """
    Serializer for detailed Group information.

    Extends the GroupSerializer to include a list of members' usernames.
    """
    members = serializers.SerializerMethodField()

    class Meta(GroupSerializer.Meta):
        fields = GroupSerializer.Meta.fields + ['members']

    def get_members(self, obj):
        return [member.username for member in obj.members.all()]


class GroupMembershipSerializer(serializers.ModelSerializer):
    """
    Serializer for GroupMembership model.

    Provides a read-only representation of GroupMembership instance.
    """
    user = serializers.ReadOnlyField(source='user.username')
    group_name = serializers.ReadOnlyField(source='group.name')
    group_id = serializers.ReadOnlyField(source='group.pk')
    joined_at = serializers.DateTimeField(
        format='%Y-%m-%d %H:%M:%S %Z', read_only=True)

    class Meta:
        model = GroupMembership
        fields = ['id', 'user', 'group_id', 'group_name', 'joined_at']
