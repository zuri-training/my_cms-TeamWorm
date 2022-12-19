from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
  def _create_user(self, email, password, username, **extra_fields):
    if not email:
      raise ValueError('The given email must be set')
    if not password:
      raise ValueError('The given password must be set')

    email = self.normalize_email(email)
    user = self.model(
      email = email,
      username = username,
      **extra_fields
    )

    user.set_password(password)
    user.save()
    return user
      
  def create_user(self, email, password, username, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_active', True)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, username, **extra_fields)

  def create_superuser(self, email, password, username, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_active', True)
    extra_fields.setdefault('is_superuser', True)
    return self._create_user(email, password, username, **extra_fields)