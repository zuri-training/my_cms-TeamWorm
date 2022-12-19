from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class RegisterForm(UserCreationForm):
  class Meta:
    model = UserProfile
    fields = [
      "email",
      'username',
      'password'
    ]
  
  
class CustomUserChangeForm(UserChangeForm):
  class Meta:
    model = UserProfile
    fields = ["email"]

