.ONESHELL:

api-bash:
	docker compose run --rm api bash

api-test:
	docker compose run --rm api make test

api-check-migrations:
	docker compose run --rm api make check-migrations

api-check:
	docker compose run --rm api make check

api-check-fix:
	docker compose run --rm api make check-fix

api-lock:
	docker compose run --rm api make lock

up:
	docker compose up -d

down:
	docker compose down

build:
	docker compose build
