from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='bookshelf_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='bookshelf_user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='bookshelf_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='bookshelf_user_permissions',
    )
