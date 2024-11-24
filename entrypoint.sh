#!/bin/sh
set -e  # on arrete le script en cas d'erreur
echo "Apply database migrations..."
python manage.py migrate --noinput

# On lance collectstatic (regroupe les static dans un rep unique)
echo "collect static files..."
python manage.py collectstatic --noinput --verbosity 2

# TODO param a mettre en variable d'env
echo "Start Gunicorn..."
exec gunicorn oc_lettings_site.wsgi:application --chdir /app/src --bind 0.0.0.0:8080