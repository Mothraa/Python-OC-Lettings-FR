"""
lettings/tests/tests_lettings_views.py
Tests for the views in lettings/views.py
"""
import pytest
from django.urls import reverse
from lettings.models import Address, Letting


@pytest.mark.unit
def test_lettings_index_view(client, monkeypatch):
    """
    Test the lettings index view with display of a list of lettings
    """
    # Mocking Profile.objects.all() to return fake profiles
    def fake_all_lettings():
        fake_lettings = [
            {"id": 1, "title": "Super appartement", "address": "1234 rue des petits pains"},
            {"id": 2, "title": "Super maison", "address": "567 avenue des radis"},
        ]
        return fake_lettings
    monkeypatch.setattr("lettings.models.Letting.objects.all", fake_all_lettings)

    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Super appartement" in response.content.decode()
    assert "Super maison" in response.content.decode()


@pytest.mark.unit
def test_letting_detail_view_unitary(client, monkeypatch):
    """
    Unitary test the letting detail view
    """
    # Mock Letting.objects.get()
    def fake_get_letting(id):
        # create fake Address
        class FakeAddress:
            number = 1234
            street = "rue des petits pains"
            city = "Paris"
            state = "NN"
            zip_code = "75000"
            country_iso_code = "FRA"

        # create fake Letting
        class FakeLetting:
            title = "Super appartement"
            address = FakeAddress()
        return FakeLetting()

    monkeypatch.setattr("lettings.models.Letting.objects.get", fake_get_letting)

    url = reverse("letting", kwargs={"letting_id": 1})
    response = client.get(url)

    assert response.status_code == 200
    assert "Super appartement" in response.content.decode()
    assert "1234 rue des petits pains" in response.content.decode()
    assert "Paris" in response.content.decode()
    assert "NN" in response.content.decode()
    assert "75000" in response.content.decode()
    assert "FRA" in response.content.decode()


@pytest.mark.integration
@pytest.mark.django_db
def test_letting_detail_view_integration(client):
    """
    Integration test for the letting detail view
    """
    # Creation de l'adresse en base
    address = Address.objects.create(
        number=1234,
        street="rue des petits pains",
        city="Paris",
        state="NN",
        zip_code="75000",
        country_iso_code="FRA",
    )

    # Creation du letting en base
    letting = Letting.objects.create(
        title="Super appartement",
        address=address,
    )

    # on accede a la vue
    url = reverse("letting", kwargs={"letting_id": letting.id})
    response = client.get(url)

    assert response.status_code == 200
    assert "Super appartement" in response.content.decode()
    assert "1234 rue des petits pains" in response.content.decode()
    assert "Paris" in response.content.decode()
    assert "NN" in response.content.decode()
    assert "75000" in response.content.decode()
    assert "FRA" in response.content.decode()

    # la suppression des données est inutile avec pytest-django / @pytest.mark.django_db
