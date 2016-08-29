cd /root/adventurelookup
git pull
docker-compose -f docker-compose.prod.yml up --build -d
docker-compose -f docker-compose.prod.yml run --rm -u root api python manage.py makemigrations
docker-compose -f docker-compose.prod.yml run --rm -u root api python manage.py migrate
docker-compose -f docker-compose.prod.yml restart nginx
