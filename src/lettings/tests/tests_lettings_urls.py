"""
lettings/tests/tests_lettings_urls.py
Tests for the urls in lettings/urls.py
"""
import pytest
from django.urls import reverse, resolve
from lettings.views import lettings_index, letting


@pytest.mark.unit
def test_lettings_index_url():
    """
    Test the lettings index URL
    """
    url = reverse("lettings_index")
    assert resolve(url).func == lettings_index


@pytest.mark.unit
def test_letting_detail_url():
    """
    Test the letting detail page URL
    """
    url = reverse("letting", kwargs={"letting_id": 1})
    assert resolve(url).func == letting
