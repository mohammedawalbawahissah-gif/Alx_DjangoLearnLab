from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    following = models.ManyToManyField(
        'self', 
        symmetrical=False,  # A follows B does not mean B follows A
        related_name='followers',  # Access all followers of a user
        blank=True
    )

    def __str__(self):
        return self.username
