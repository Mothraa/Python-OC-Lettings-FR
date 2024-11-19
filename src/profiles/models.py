"""
profiles/models.py

Module that defines the models for the profiles app

Models:
    - Profile: Extend attributes (favorite city) of the django User model
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Represents an app user profile

    Attributes:
        user (User): link with a Django User model
        favorite_city (str): The user's favorite city. max length 64 chars
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Returns the string representation of the profile

        Returns:
            str: The username of the User
        """
        return self.user.username

    class Meta:
        """
        Meta options for the Profile model

        Attributes:
            managed (bool): Specify if the model is managed by django's migrations
            => set to False
        """
        managed = False
