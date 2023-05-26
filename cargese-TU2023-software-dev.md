---
marp: true
theme: default
class: invert
size: 16:9
paginate: true
---

# Software Development

> How to bring your (python) codes to the next level

Nicolas Dagoneau - nicolas.dagoneau@cea.fr

Transient Universe 2023 - Cargèse

---

# Introduction

## About me

- PhD on Svom (2017-2020): image processing for the ECLAIRs onboard trigger, study GRBs detection (ultra-long GRBs).
- Since 2021: working at CEA, computer division, on Svom and Euclid (science & development).

## Goal of this presentation

- Show you how to turn bunch of python files to package, ready to be shared, tested and documented.
- Based on my own experience (hence biased).

---

# Why?

During my PhD, the code I wrote was mainly python files (modules) + some jupyter notebooks (always changing) in different directories: not always backed-up, not documented, very few constrains on code quality, few or no test at all &rarr; difficult to maintain and to share.

---

# Tools

- Use an integrated development environment: [pycharm](https://www.jetbrains.com/fr-fr/pycharm/), [VSCode](https://code.visualstudio.com/)...
- Define package: [setuptools](https://setuptools.pypa.io)
- Implement tests (in parallel to the development): [pytest](https://docs.pytest.org), using `assert`
- Code coverage by the tests: [coverage](https://coverage.readthedocs.io/en/latest/)
- Write the documentation: [sphinx](https://www.sphinx-doc.org)/[ReadTheDocs](https://docs.readthedocs.io)
- Autoformat code: [black](https://black.readthedocs.io/en/stable/)
- Analyse code: [pylint](https://pylint.readthedocs.io/en/latest/), [ruff](https://beta.ruff.rs/docs/), [flake8](https://flake8.pycqa.org/en/latest/)...
- Push to git: [github](https://github.com/), [gitlab](https://gitlab.com)

---

# Package structure

Basic package structure.

    ├── pyproject.toml
    ├── README.md
    ├── requirements.txt
    ├── doc
    ├── src
    │   └── cargese
    │       ├── gcn_requester.py
    │       ├── __init__.py
    │       └── tools.py
    ├── tests
    │   ├── test_gcn_requester.py
    │   └── test_tools.py

---

# Write tests

Tests should be simple, short, easy to understand and allow to cover all cases in the code (*if, else*, *for*, raised exceptions...). They use `assert`.

### Example:

```python
def test_timestamp_to_datetime():
    utc_date = tools.timestamp_to_datetime(0)
    assert utc_date == datetime.datetime(1970, 1, 1)
```

---

# Install, test, build documentation

```bash
black src/
ruff check src/  # pylint src/
pip install .
pytest tests/
coverage run --source src/ -m pytest
coverage report
cd doc && make html # or other format
```

--- 

# All together with `make`

*Makefile:*: `make install`, `make test`...

```Makefile
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
```

---

# Continuous integration: push, build, test, deploy

You can build wathever you want (eg. building pdf for PhD manuscript).

## Running in a distant repository

Jobs (install, checks, tests, ...) are described in yaml files.

- On github, it works with *actions*, stored in `.github/workflows`.
- On gitlab, it works with `.gitlab-ci.yml`

---

# Lets practice

- Fork [github.com/dagnic/cargese-TS2023-dev](https://github.com/dagnic/cargese-TS2023-dev)
- (Create conda env: `conda create -n cargese python=3.10`)
- Install requirements: `pip install -r requirements.txt`

## Exercise

Implement a new method/class, install, add tests and run them, generate documentation, (use `make`) push and check that jobs succeed!

---

# Few configurations

- Activate github pages on `gh-pages` branch (https://github.com/<user>/<project>/settings/pages). Documentation is here: https://<user>.github.io/<project>/
- Add your repository to [coveralls.io](https://coveralls.io/)

---

# To go further away

- For other languages (eg. C++), you could create bindings to access C++ class via python: [pybind11](https://pybind11.readthedocs.io/en/stable/), [swig](https://www.swig.org/).
- Create your own dashboard to plot results using [plotly/dash](https://dash.plotly.com)
- Licence for software distribution: that's someting you have to ask yourself about if you want to share your package within the publid domain.
- Publish package to PyPI: [twine](https://twine.readthedocs.io/en/latest/) 
- Things can alway be improved: find a balance
- Code design and factoring is also an important job
- Version number update: [bump2version](https://github.com/c4urself/bump2version/)
- Changelog

---

... __"Be kinder to your future self"__ *(ruff)*

