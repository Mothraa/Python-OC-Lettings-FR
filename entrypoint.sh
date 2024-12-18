#!/bin/sh
# TODO desactivé car erreurs avec static manquants mais ref dans le css (bg-waves.svg)
# set -e  # on arrete le script en cas d'erreur

echo "Apply database migrations..."
python src/manage.py migrate --noinput

# On lance collectstatic (regroupe les static dans un rep unique)
echo "collect static files..."
python src/manage.py collectstatic --noinput --verbosity 2

# TODO param a mettre en variable d'env
echo "Start Gunicorn..."
exec gunicorn oc_lettings_site.wsgi:application --chdir /app/src --bind 0.0.0.0:8080