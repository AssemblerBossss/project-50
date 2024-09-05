#Makefile
install:
	poetry install

build:
	poetry build

gendiff:
	poetry run gendiff

publish:
	poetry publish --d

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest

