# Fileparser Projekt


## Installation
uv sync
pre-commit install
pre-commit run --all-files

## Nutzung als selbststehendes Programm
Der folgende Aufruf funktioniert nur deshalb, weil '__main__.py' implementiert ist.

uv run -m fileparser example.txt


## Nutzung als Import
Wenn das Projekt z.B. via PyPi oder Github installiert wird,
dann soll es so genutzt werden:

from fileparser import parse

(der direkte Import von parse geht desdhalb, weil wir in fileparser/__init__.py dioe parse-Fkt. vorgeladen haben.)

## Testen
uv run pytest -v -s

## aus github installieren

pip install git+https://github.com/packaging-kurs/fileparser.git@main