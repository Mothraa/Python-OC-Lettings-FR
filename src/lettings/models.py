"""
lettings/models.py

Module that defines the models for the lettings app

Models:
    - Address: represents an address associated with a letting
    - Letting: represents a letting with a title and associated to an address.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Represents an address of a letting

    Attributes:
        number (int): address street number. max 4 digits
        street (str): address street name. max length 64 chars
        city (str):  address city name. max length 64 chars
        state (str): state code with 2 chars. e.g. : "PA"
        zip_code (int): address zip code. Max 5 digits
        country_iso_code (str): code for country with 3 chars. e.g. : "USA"
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Returns the string representation of the address

        Returns:
            str: The address street number and name
        """
        return f'{self.number} {self.street}'

    class Meta:
        """
        Meta options for the Address model

        Attributes:
            managed (bool): Specify if the model is managed by django's migrations
            => set to False
            verbose_name_plural (str): manage specific plural for admin interface
            plural of "address" set to "addresses"
        """
        managed = False
        verbose_name_plural = "adresses"


class Letting(models.Model):
    """
    Represents a letting

    Attributes:
        title (str): title name of the letting. max length 256 chars
        address (OneToOneField): the address associated with the letting
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation of the letting

        Returns:
            str: The title name of the letting
        """
        return self.title

    class Meta:
        """
        Meta options for the Letting model

        Attributes:
            managed (bool): Specify if the model is managed by django's migrations
            => set to False
        """
        managed = False
