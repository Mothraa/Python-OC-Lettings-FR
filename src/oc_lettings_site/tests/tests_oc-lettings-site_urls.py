"""
oc_lettings_site/tests/tests_oc-lettings-site_urls.py
Tests for the urls in oc_lettings_site/urls.py
"""
import pytest
from django.urls import reverse, resolve

from oc_lettings_site.views import index


@pytest.mark.unit
def test_index_url():
    """
    Test the home page URL
    """
    url = reverse("index")
    assert resolve(url).func == index


@pytest.mark.unit
def test_custom_404_handler(client):  # fixture client présente dans pytest-django
    """
    Test the custom 404 error handler by accessing a fake URL.
    """
    response = client.get("/fakepage/")
    assert response.status_code == 404
    assert "Page Not Found (error 404)" in response.content.decode()
