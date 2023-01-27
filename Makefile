.PHONY : requirements.sync tests

requirements.sync : requirements.txt
	pip-sync

requirements.txt : requirements.in setup.py
	pip-compile

tests :
	pytest -v
