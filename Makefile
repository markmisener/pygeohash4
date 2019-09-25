SHELL := /bin/bash

.PHONY: install clean test pre-commit

venv:
	virtualenv --python=python3.6 venv

install: venv
	source venv/bin/activate; \
	pip install -r ./test/requirements.txt;

clean:
	rm -r venv/

test:
	make pre-commit
	sh test/test.sh

pre-commit: install
	source venv/bin/activate; \
	pre-commit run --all-files
