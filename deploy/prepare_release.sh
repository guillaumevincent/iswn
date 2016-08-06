#!/bin/bash

echo "prepare release"
cd ..

echo "build dev docker compose"
docker-compose stop
docker-compose rm -f
docker-compose pull
docker-compose build
docker-compose up -d

echo "install dev depencies"
docker exec iswn_frontend_1 npm install

echo "run test"
docker exec iswn_frontend_1 npm run test
docker exec iswn_backend_1 python manage.py test

echo "run build"
docker exec iswn_frontend_1 npm run build
sudo chown -R $USER:$USER .

git status
cd deploy
