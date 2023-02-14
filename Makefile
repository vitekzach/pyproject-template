include .vars/variables_nonsensitive.env
include .vars/variables_sensitive.env


activate:
	@poetry shell

install:
	@echo "Installing..."
	@$(MAKE) setup-poetry

setup-poetry:
	@poetry env use python3 && poetry install

test:
	@echo "\e[4;36m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++PYTEST++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[0m"
	@poetry run python -m pytest --cov=${PROJECT_NAME} --cov-report=html
	@echo "\e[4;36m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++BANDIT++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[0m"
	@poetry run python -m bandit -r -x tests ${PROJECT_NAME}

format:
	@echo "\e[4;36m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ISORT++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[0m"
	@poetry run python -m isort --profile=black ${PROJECT_NAME} tests
	@echo "\e[4;36m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++FLAKE8++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[0m"
	@poetry run python -m flake8 --max-line-length=120 ${PROJECT_NAME} tests
	@echo "\e[4;36m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++PYDOCSTYLE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[0m"
	@poetry run python -m pydocstyle --convention=numpy ${PROJECT_NAME} tests
	@echo "\e[4;36m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++MYPY+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[0m"
	@poetry run python -m mypy --ignore-missing-imports --no-namespace-packages ${PROJECT_NAME} tests
	@echo "\e[4;36m+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++PYLINT++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\e[0m"
	@poetry run python -m pylint --recursive=y --max-line-length=120 --include-naming-hint=y ${PROJECT_NAME} tests

docs:
	@poetry run pdoc --	 ${PROJECT_NAME} -o docs
	@echo "Saved documentation."

view-docs:
	@echo "Viewing API documentation..."
	@echo "TODO fix?"

run:
	@poetry run python ${PROJECT_NAME}/main.py

start:
	@poetry run uvicorn ${PROJECT_NAME}.server.server:app --reload

start-logging-stack:
	@docker compose up -d

precommit:
	@pre-commit install && pre-commit run --all-files

poetry-packages:
	@poetry check
	@poetry lock
	@poetry export -orequirements.txt --without-hashes --without-urls
