from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    """
    Model representing a group.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(
        User, through='GroupMembership', related_name='group_memberships')
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_groups')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Group: {self.name}"


class GroupMembership(models.Model):
    """
    Model representing the membership of a user in a group.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.group.name}"
