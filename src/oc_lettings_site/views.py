"""
oc_lettings_site/views.py
Contains the Django views for rendering the home page and custom error pages.
"""
from django.shortcuts import render


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


def custom_404(request, exception):
    """
    Handling custom 404 error page

    Args:
        request (HttpRequest): HTTP request object
        exception (Exception): the exception that caused the 404 error

    Returns:
        HttpResponse: The rendered 404 error page with a 404 status code
    """
    # TODO handle exception with sentry
    return render(request, "404.html", status=404)


def custom_500(request):
    """
    Handling custom 500 error page

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: The rendered 500 error page with a 500 status code
    """
    return render(request, "500.html", status=500)
