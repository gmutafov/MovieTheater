from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.validators import validate_capitalized, only_letters
from movies.models import Movie


from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='appuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='appuser_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

