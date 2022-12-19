from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .authentication import CustomUserManager
from django.conf  import settings



# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    username=models.CharField(max_length=50)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50, unique=True)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    instagram_link = models.CharField(max_length=150, blank=True)
    twitter_link = models.CharField(max_length=150, blank=True)
    
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  = ['username', 'password']
    
    
    
    


    def __str__(self) -> str:
        return f"<{self.username}>, <{self.id}>"
    