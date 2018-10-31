all: run tests

develop:
	pipenv run python setup.py develop


tests: unit functional

unit functional:
	nosetests tests/$@

run: develop
	unpyguetti -i examples.definitions -l examples/definitions.py examples/test/test_1.py
