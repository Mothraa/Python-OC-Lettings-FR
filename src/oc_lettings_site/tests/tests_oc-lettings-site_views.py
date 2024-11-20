"""
oc_lettings_site/tests/tests_oc-lettings-site_views.py
Tests for the views in oc_lettings_site/views.py
"""
import pytest
from django.urls import reverse
from django.test.utils import override_settings


@pytest.mark.unit
@override_settings(DEBUG=False)
def test_index_view(client):  # fixture client présente dans pytest-django
    """
    Test the home page view
    """
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert "Holiday Homes" in response.content.decode()


@pytest.mark.unit
@override_settings(DEBUG=False)
def test_custom_404_view(client):  # fixture client présente dans pytest-django
    """
    Test the custom 404 error page view
    """
    response = client.get("/fakepage/")
    assert response.status_code == 404
    assert "Page Not Found (error 404)" in response.content.decode()
