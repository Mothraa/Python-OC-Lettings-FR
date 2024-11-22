import os


def load_django():
    """
    Load Django if necessary
    Usefull for generating docs for example with sphinx autodoc.
    Deactivate for readthedoc (env variable : SKIP_DJANGO==1)
    """
    # if os.getenv('SKIP_DJANGO') == '1':
    #     return

    try:
        import django

        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "oc_lettings_site.settings")
        django.setup()
    except Exception as e:
        print(f"Erreur chargement Django {e}")
