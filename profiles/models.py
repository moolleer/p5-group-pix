from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver


class Profile(models.Model):
    """
    Model representing user profiles.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to='images/', default='../default_profile_eianob'
    )

    class Meta:
        ordering = ['-join_date']

    def __str__(self):
        return f"{self.owner}'s profile"


# Signal handler function to create a profile when a new user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


# Signal handler function to update the last_login field in Profile
@receiver(user_logged_in)
def update_last_login(sender, request, user, **kwargs):
    try:
        profile = Profile.objects.get(owner=user)
        profile.last_login = user.last_login
        profile.save()
    except Profile.DoesNotExist:
        pass


post_save.connect(create_profile, sender=User)
user_logged_in.connect(update_last_login)
