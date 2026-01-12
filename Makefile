VENV=venv
PYTHON=../$(VENV)/Scripts/python.exe
PIP=../$(VENV)/Scripts/pip.exe

.PHONY: venv

venv: 
	python -m venv $(VENV)

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) src/convert_pdfs.py
