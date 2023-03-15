import os
import uuid
from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ImageField


class CustomUser(AbstractUser):
    def has_profile(self) -> bool:
        return hasattr(self, 'profile') and self.profile is not None


def get_upload_path(_, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'
    return os.path.join(datetime.now().strftime('uploads/%Y/%m/%d/avatar'), filename)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    shortname = models.SlugField(max_length=10, unique=True, null=True, blank=True)
    status = models.TextField(max_length=300, default='', blank=True)
    avatar = ImageField(upload_to=get_upload_path, default='avatar.jpg', blank=True)

    def __str__(self):
        return self.shortname or f'nick-{self.nickname}'
