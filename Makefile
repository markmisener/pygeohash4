SHELL := /bin/bash

.PHONY: install clean test-local

venv:
	virtualenv --python=python3.6 venv

clean:
	rm -r venv/

install: venv
	source venv/bin/activate; \
	pip install -r ./test/requirements.txt; \

test-local:
	sh test/test.sh
