#!/bin/bash

if [ $1 = 'dev' ]; then
    exec docker-compose -f docker-compose.dev.yml up "${@:2}"
elif [ $1 = 'build' ]; then
    if [ $2 = 'dev' ]; then
        exec docker-compose -f docker-compose.dev.yml build "${@:3}"
    elif [ $2 = 'prod' ]; then
        exec docker-compose -f docker-compose.prod.yml build "${@:3}"
    fi
fi
