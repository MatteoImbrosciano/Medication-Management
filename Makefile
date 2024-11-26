# Task per installare le dipendenze usando Poetry
install:
	poetry install

# Task per controllare la sintassi dei file Python
check:
	python check_syntax.py

# Task per eseguire i test
test:
	poetry run pytest

# Task per eseguire tutti i task
all: install check test
