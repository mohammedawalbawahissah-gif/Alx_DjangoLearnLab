from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='bookshelf_user_set',  # custom related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='bookshelf_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='bookshelf_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='bookshelf_user_permissions'
    )
