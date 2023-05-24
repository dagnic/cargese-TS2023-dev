help:
	@echo 'Usage: make <COMMAND>'
	@echo ''
	@echo 'Commands'
	@echo '    install:  install package'
	@echo '    sphinx:   build sphinx documentation'
	@echo '    test:     run tests and show report'
	@echo '    coverage: measure coverage and display report'
	@echo '    clean:    remove build files'
	@echo '    all:      install, test, coverage, sphinx'

.PHONY: all
all: install test sphinx coverage

install:
	@pip install .

test:
	@pytest tests

sphinx:
	@make -C doc/ html

coverage:
	@coverage run --source src/cargese -m pytest
	@coverage report

clean:
	@rm -rf .pytest_cache .ruff_cache build doc/_build doc/api src/cargese.egg-info .coverage