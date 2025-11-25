.PHONY: install lint fmt test typecheck run hooks allure
install:
	pip install -U pip && pip install -e .[dev]

fmt:
	black . && isort .

lint:
	ruff check .

typecheck:
	mypy .

test:
	pytest

hooks:
	pre-commit install --hook-type pre-commit --hook-type pre-push

run:
	uvicorn app.main:app --reload

allure:
	pytest --alluredir=allure-results && allure serve allure-results
