from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    instagram_link = models.CharField(max_length=150, blank=True)
    twitter_link = models.CharField(max_length=150, blank=True)


    def __str__(self) -> str:
        return f"<{self.username}>, <{self.id}>"