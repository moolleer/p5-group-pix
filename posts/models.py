from django.db import models
from django.contrib.auth.models import User
from groups.models import Group


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set to always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_e3pet6.jpg', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return (
            f"Post: {self.title} - by {self.owner.username} "
            f"in {self.group.name}"
        )
