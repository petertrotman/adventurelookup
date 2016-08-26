#!/bin/bash
set -e
cd /code

if [ "$ENV" = 'DEV' ]; then
    echo "Building development files."
    npm run build:dev
    echo "Running development server."
    exec npm start
else
    echo "Building production files"
    exec npm run build:prod
fi

