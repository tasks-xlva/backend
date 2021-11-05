start:
	docker compose up -d ${args}

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate
