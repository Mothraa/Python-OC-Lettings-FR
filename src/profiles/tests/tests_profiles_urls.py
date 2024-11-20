"""
profiles/tests/tests_profiles_urls.py
Tests for the urls in profiles/urls.py
"""
import pytest
from django.urls import reverse, resolve
from profiles.views import index, profile


@pytest.mark.unit
def test_profiles_index_url():
    """
    Test the URL for the profiles index page.
    """
    url = reverse("profiles_index")
    assert resolve(url).func == index


@pytest.mark.unit
def test_profile_detail_url():
    """
    Test the URL for the profile detail page.
    """
    url = reverse("profile", kwargs={"username": "Utilisateur_test"})
    assert resolve(url).func == profile
