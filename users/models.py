from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to="users/avatar/%Y/%m/%d", blank=True, verbose_name="Аватар")

    def __str__(self):
        return self.username
