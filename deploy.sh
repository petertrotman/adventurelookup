cd /root/adventurelookup
git pull
docker-compose -f docker-compose.prod.yml up --build -d
docker-compose -f docker-compose.prod.yml restart nginx
