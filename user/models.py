from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    background_color = models.CharField(max_length=7, default="#ffffff")

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Storyboard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='storyboards')
    text = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='storyboard_photos/', blank=True, null=True)
    video = models.FileField(upload_to='storyboard_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Storyboard by {self.user.username} at {self.created_at}"

class Friendship(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name='friendships_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name='friendships_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user.username} is friends with {self.to_user.username}"
