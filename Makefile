# build server
.PHONY: docker-build
docker-build:
	docker compose build --build-arg REQUIREMENTS_NAME=local

# run server
.PHONY: docker-up
docker-up:
	docker compose up

# stop server
.PHONY: docker-down
docker-down:
	docker compose down

# docker prompt
.PHONY: docker-shell
docker-shell:
	docker exec -it ciaglo-django /bin/bash


# docker test
.PHONY: docker-test
docker-test:
	docker exec -it ciaglo-django ./manage.py test

.PHONY: flake8
## PEP8 check using flake8.
flake8:
	flake8 apps

.PHONY: pylint
## Perform static analysis using pylint.
pylint:
	pylint -j 0 apps

.PHONY: black-check
## black is used to check code style
black-check:
	black --exclude migrations --check config apps

.PHONY: black-fix
## Use black to correct code style issues.
black-fix:
	black config apps --exclude migrations

.PHONY: isort-check
## Use isort to check import ordering
isort-check:
	isort -c -rc apps

.PHONY: isort-fix
## Automatically rewrite import ordering using isort.
isort-fix:
	isort -rc apps