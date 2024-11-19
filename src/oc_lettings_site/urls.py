"""
oc_lettings_site/urls.py
Defines URL routes and error handling for the main app.

URL paths:
    '' : Home page
    'lettings/' : Includes the URLs from the "lettings" app
    'profiles/' : Includes the URL patterns from the "profiles" app
    'admin/' : Django's admin interface

Error handlers:
    404 : Custom view for handling 404 errors
    500 : Custom view for handling 500 errors
"""

from django.contrib import admin
from django.urls import path, include

from . import views

# Custom handler for 404 errors => specifies the view to render
handler404 = "oc_lettings_site.views.custom_404"

# Custom handler for 500 errors => specifies the view to render
handler500 = "oc_lettings_site.views.custom_500"

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
