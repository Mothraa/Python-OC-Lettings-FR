"""
oc_lettings_site/views.py
Contains the Django views for rendering the home page and custom error pages.
"""
import logging

from django.shortcuts import render
from django.http import JsonResponse

logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
# eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
# pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna,
# non finibus neque cursus id.

def index(request):
    """
    Render the home page of the app.

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: The rendered home page (index.html)
    """
    return render(request, 'oc_lettings_site/index.html')


def health(request):
    """
    Health check view for testing deploiement

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        JsonResponse: Json response with status code 200
    """
    logger.info("Health check endpoint accessed.")
    # TODO : add db connect try
    return JsonResponse({"status": "ok"}, status=200)


def custom_404(request, exception):
    """
    Handling custom 404 error page

    Args:
        request (HttpRequest): HTTP request object
        exception (Exception): the exception that caused the 404 error

    Returns:
        HttpResponse: The rendered 404 error page with a 404 status code
    """
    logger.warning(f"404 error. Path: {request.path}. Exception: {exception}")
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Handling custom 500 error page

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: The rendered 500 error page with a 500 status code
    """
    print("=== Entering custom_500 handler ===")
    print("Request path:", request.path)
    print("Request method:", request.method)
    logger.critical(f"500 error. Path: {request.path}, Method: {request.method}")
    return render(request, "500.html", status=500)
