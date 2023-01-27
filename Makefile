.PHONY : requirements.sync

requirements.sync : requirements.txt
	pip-sync

requirements.txt : requirements.in setup.py
	pip-compile
