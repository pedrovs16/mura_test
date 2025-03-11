folder=$(shell basename $(CURDIR))
app_name=$(folder)-app-1
worker_name=$(folder)-celery_worker-1
db_volume_name=$(folder)_postgres-data

default: build up_d

build:
	docker compose -f ./compose.common.yml -f ./compose.dev.yml build

up:
	docker compose -f ./compose.common.yml -f ./compose.dev.yml up

up_d:
	docker compose -f ./compose.common.yml -f ./compose.dev.yml up -d

down:
	docker compose -f ./compose.common.yml -f ./compose.dev.yml down

stop:
	docker compose -f ./compose.common.yml -f ./compose.dev.yml stop

restart:
	docker compose -f ./compose.common.yml -f ./compose.dev.yml restart

logs:
	docker logs $(app_name) -f

bash:
	docker exec -it $(app_name) bash

fmt:
	docker exec -t $(app_name) bash -c "black . && isort . --overwrite-in-place"

lint:
	docker exec -t $(app_name) ruff check .

lint_fix:
	docker exec -t $(app_name) ruff check . --fix

mypy:
	docker exec -t $(app_name) bash -c "mypy ."

test:
	docker exec -it $(app_name) python -m pytest -vv -s --show-capture=no $(path)

test_debug:
	docker exec -it $(app_name) python -m pytest -vv $(path)

migrations:
	docker exec -it $(app_name) alembic revision --autogenerate -m "$(msg)"

migrate:
	docker exec -it $(app_name) alembic upgrade head

downgrade:
	docker exec -it $(app_name) alembic downgrade -1

delete_db:
	docker volume rm $(db_volume_name)
