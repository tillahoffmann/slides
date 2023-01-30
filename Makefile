.PHONY : requirements.sync sdist tests

requirements.sync : requirements.txt
	pip-sync

requirements.txt : requirements.in setup.py
	pip-compile

tests :
	pytest -v

lint :
	flake8

sdist :
	python setup.py sdist
	twine check dist/*.tar.gz
