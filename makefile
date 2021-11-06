install:
	pip install -r requirements/local.txt

start:
	docker-compose up -d

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

cert:
	./init-letsencrypt.sh

production:
	docker-compose -f production.yml up -d --build
