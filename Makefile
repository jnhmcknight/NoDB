.PHONY: clean install is_newest_version tests publish all

all: install tests

clean:
	find . -name "*.py[c|o]" -o -name __pycache__ -exec rm -rf {} +
	-rm -rf dist
	-rm -rf *.egg-info

install:
	pip install -e .[dev]

is_newest_version:
	python is_newest_version.py

tests:
	python setup.py pytest

publish: is_newest_version clean
	pip install twine
	python setup.py sdist
	twine upload --skip-existing dist/*
