up:
	docker-compose up --build
test:
	docker exec -it django_api sh -c "python manage.py test"