PYTHON=./venv/bin/python
PIP=./venv/bin/pip

.PHONY: install-build-requirements build

install-build-requirements:
	$(PIP) install wheel

build: install-build-requirements
	$(PYTHON) setup.py sdist bdist_wheel

clean:
	rm -rf build/ dist/ *.egg-info/
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete