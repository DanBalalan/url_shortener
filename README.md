### url_shortener

run server at 0.0.0.0:8000:
docker-compose up --build


if you need to update db:
docker-compose run api python /code/manage.py makemigrations
docker-compose run api python /code/manage.py migrate