from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from discussions.models import Discussion


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='posts',
        null=True, blank=True)
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name='comments',
        null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
