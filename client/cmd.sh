#!/bin/bash
set -e
cd /code

if [ "$ENV" = 'DEV' ]; then
    echo "Building Production Files & Running Development Server."
    npm run build:dev
    exec npm start
else
    echo "Building Production Files"
    exec npm run build:prod
fi

