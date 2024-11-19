"""
lettings/urls.py
Defines URL routes for the lettings app.

URL paths:
    '' : Main lettings page (with list of all lettings)
    '<int:letting_id>/' : details for a specific letting
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.lettings_index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
