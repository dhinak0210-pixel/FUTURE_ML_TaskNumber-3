.PHONY: install test lint format run-api run-dashboard clean

install:
	poetry install

test:
	poetry run pytest tests/

lint:
	poetry run black src/ tests/ --check
	poetry run isort src/ tests/ --check-only
	poetry run flake8 src/ tests/
	poetry run mypy src/

format:
	poetry run black src/ tests/
	poetry run isort src/ tests/

run-api:
	poetry run uvicorn src.resume_ml.api.fastapi_app:app --reload

run-dashboard:
	poetry run streamlit run app.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf site/
