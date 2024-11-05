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

compose-up:
	docker compose up -d

compose-down:
	docker compose down

compose-build:
	docker compose build
