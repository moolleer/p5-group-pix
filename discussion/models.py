from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class Discussion(models.Model):
    """
    Discussion model related to Group and User
    """
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
