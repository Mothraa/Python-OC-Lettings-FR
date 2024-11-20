"""
lettings/tests/tests_lettings_models.py
Tests for the models in lettings/models.py
"""
import pytest
from lettings.models import Address, Letting


@pytest.mark.unit
def test_address_model():
    """
    Test the Address model through the __str__ representation
    """
    fake_address = Address(number=1234, street="rue des petits pains")

    assert str(fake_address) == "1234 rue des petits pains"


@pytest.mark.unit
def test_letting_model():
    """
    Test the Letting model through the __str__ representation
    """
    fake_address = Address(number=1234, street="rue des petits pains")
    fake_letting = Letting(title="Super appartement", address=fake_address)

    assert str(fake_letting) == "Super appartement"
