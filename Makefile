##@ Code checks and formatting
format/isort:: ## Format your code with isort
	poetry run isort .

format/black:: ## Format your code with black
	poetry run black .

format: format/isort format/black ## Format your code with isort and black

mypy:: ## Run mypy check
	poetry run mypy

lint:: ## Run all code checks
	poetry run mypy src
	poetry run flake8 src
	poetry run black --check .
	poetry run isort . -c

##@ Tests
test:: ## Run tests
	poetry run pytest