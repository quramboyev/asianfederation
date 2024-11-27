.ONESHELL:

install:
	poetry install --with dev --no-root

lock:
	poetry lock

test:
	pytest --no-migrations

check-migrations:
	python manage.py makemigrations --check --dry-run

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --noinput

check:
	black . --check \
	&& ruff check . \
	&& safety check \
	&& make check-migrations \

check-fix:
	black .
	ruff check --fix-only --show-fixes --statistics .

run_crontab:
	service cron start && python manage.py crontab add

run: migrate collectstatic
	python manage.py runserver 0.0.0.0:8000

run_server: collectstatic migrate
	gunicorn project.config.wsgi:application --bind 0.0.0.0:8000
