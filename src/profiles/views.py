"""
profiles/views.py
Contains the Django views for rendering the profiles main page (list) and specific profile pages.
"""
from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex, sed consequat libero pulvinar eget.
# Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Render the profiles index page, display a list of all profiles

    Args:
        request (HttpRequest): HTTP request object

    Returns:
        HttpResponse: render profiles index page (index.html) with a list of profiles
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui.
# Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant
# morbi tristique senectus et netus et males
def profile(request, username):
    """
    Render the profile detail page for a specific user

    Args:
        request (HttpRequest): HTTP request object
        username (str): the username of the profile to display

    Returns:
        HttpResponse: render profile detail page (profile.html)
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
