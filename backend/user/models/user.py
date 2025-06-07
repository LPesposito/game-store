from django.contrib.auth.models import AbstractUser
from django.db import models


def user_profile_image_path(instance, filename):
    return f'user_{instance.id}/profile/{filename}'


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=50, unique=True)
    profile_image = models.ImageField(
        upload_to=user_profile_image_path,
        blank=True,
        null=True,
        default='default/avatar.png'  
    )

    def __str__(self):
        return self.username or self.email