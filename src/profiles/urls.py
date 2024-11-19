"""
profiles/urls.py
Defines URL routes for the profiles app.

URL paths:
    '' : Main profiles page (with list of all profiles)
    '<str:username>/' : details for a specific profile
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
