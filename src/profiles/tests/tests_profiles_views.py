"""
profiles/tests/tests_profiles_views.py
Tests for the views in profiles/views.py
"""
import pytest
from django.urls import reverse
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.unit
def test_profiles_index_view(client, monkeypatch):
    """
    Test the profiles index view with display of a list of profiles
    """
    # Mocking Profile.objects.all() to return fake profiles
    def fake_all_profiles():
        fake_profiles = [
            type("Profile", (), {"user": type("User", (), {"username": "user1"}), "favorite_city": "Paris"}),
            type("Profile", (), {"user": type("User", (), {"username": "user2"}), "favorite_city": "London"}),
        ]
        return fake_profiles
    monkeypatch.setattr("profiles.models.Profile.objects.all", fake_all_profiles)

    url = reverse("profiles_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Profiles" in response.content.decode()
    assert "user1" in response.content.decode()
    assert "user2" in response.content.decode()
    # message affiché dans le cas ou il n'y aurait pas de données
    assert "No profiles are available." not in response.content.decode()


@pytest.mark.unit
def test_profile_detail_view_unitary(client, monkeypatch):
    """
    Unitary test the profile detail view
    """
    # mock Profile.objects.get()
    def fake_get_profile(**kwargs):
        class FakeUser:
            username = "Utilisateur_test"
            first_name = "Michel"
            last_name = "Letesteur"
            email = "michel.letesteur@test.com"

        class FakeProfile:
            user = FakeUser()
            favorite_city = "Paris"

        return FakeProfile()

    monkeypatch.setattr("profiles.models.Profile.objects.get", fake_get_profile)

    url = reverse("profile", kwargs={"username": "Utilisateur_test"})
    response = client.get(url)

    assert response.status_code == 200
    assert "Utilisateur_test" in response.content.decode()
    assert "Michel" in response.content.decode()
    assert "Letesteur" in response.content.decode()
    assert "michel.letesteur@test.com" in response.content.decode()
    assert "Paris" in response.content.decode()
    # on regarde si le bouton Back est présent dans la page
    assert "Back" in response.content.decode()


@pytest.mark.integration
@pytest.mark.django_db
def test_profile_detail_view_integration(client):
    """
    Integration test of the profile detail view
    """
    # creation d'un utilisateur en base
    user = User.objects.create(username="Utilisateur_test",
                               first_name="Michel",
                               last_name="Letesteur",
                               email="michel.letesteur@test.com"
                               )
    # creation d'un profile en base
    Profile.objects.create(user=user, favorite_city="Paris")

    # on accede a la vue
    url = reverse("profile", kwargs={"username": "Utilisateur_test"})
    response = client.get(url)

    assert response.status_code == 200
    assert "Utilisateur_test" in response.content.decode()
    assert "Michel" in response.content.decode()
    assert "Letesteur" in response.content.decode()
    assert "michel.letesteur@test.com" in response.content.decode()
    assert "Paris" in response.content.decode()
    # on regarde si le bouton Back est présent dans la page
    assert "Back" in response.content.decode()

    # la suppression des données est inutile avec pytest-django / @pytest.mark.django_db
