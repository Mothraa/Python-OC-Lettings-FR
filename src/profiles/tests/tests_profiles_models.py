"""
profiles/tests/tests_profiles_models.py
Tests for the models in profiles/models.py
"""
import pytest
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.unit
def test_profile_model():
    """
    Test the Profile model through the __str__ representation
    """
    fake_user = User(username="Utilisateur_test")
    fake_profile = Profile(user=fake_user, favorite_city="Paris")

    assert str(fake_profile) == "Utilisateur_test"
    assert fake_profile.favorite_city == "Paris"
