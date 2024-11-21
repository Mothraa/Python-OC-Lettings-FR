#!/bin/sh

echo "Applying database migrations..."
python manage.py migrate --noinput

# On lance collectstatic (regroupe les static dans un rep unique)
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec gunicorn oc_lettings_site.wsgi:application --chdir /app/src --bind 0.0.0.0:8080