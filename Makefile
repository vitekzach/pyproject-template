include variables.env


activate:
	@echo "TODO Activating poetry shell"

install:
	@echo "Installing..."
	@$(MAKE) setup-poetry

setup-poetry:
	@poetry env use python3 && poetry install

test:
	@poetry run python -m pytest .
	#&& readme-cov
	@echo "TODO GENERATE HTML REPORT"

format:
	@echo "TODO Formatting python code"
	#isort
	#flake8
	#pydocstyle
	#mypy
	#pylint
	@echo "____________________________________________________________BANDIT____________________________________________________________"
	@poetry run python -m bandit -r -x tests ${PROJECT_NAME}

docs:
	@poetry run pdoc --html ${PROJECT_NAME} -o docs
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

coverage:
	@poetry run python -m pytest --cov=${PROJECT_NAME} --cov-report=html
