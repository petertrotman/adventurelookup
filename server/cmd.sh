#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    exec uwsgi --ini /code/uwsgi.ini:dev
else
    echo "Running Production Server"
    exec uwsgi --ini /code/uwsgi.ini:prod
fi
