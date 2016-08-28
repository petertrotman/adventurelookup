#!/bin/bash
set -e

echo "Collect static files"
python /code/manage.py collectstatic --no-input

if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    exec uwsgi --ini /code/uwsgi.ini:dev
else
    echo "Running Production Server"
    exec uwsgi --ini /code/uwsgi.ini:prod
fi
