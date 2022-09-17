# cookiecutter-dsci

<!-- badges: start -->
[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
<!-- badges: end -->

Cookiecutter for data science projects by Ephel. The main objective of this cookiecuter is to use the dataflow with
[Prefect].

## Features

The primary packages, used to manage the template and environment are the following

|package|description|
|:-----|:-----------------|
|[cookiecutter]|Project templates|
|[poetry]|Project dependency|

The packages used to ensure code quality and documentation are

|package|description|
|:-----|:-----------------|
|[flake8]|Style guide enforcement|
|[pep8-naming]|Check PEP-8 naming conventions, plugin for `flake8`|
|[black]|Code formatter|
|[pre-commit]|Manage pre-commit hooks|
|[pre-commit-hooks]|Some out-of-the-box hooks for `pre-commit`|
|[pytest]|Framework for testing|
|[mypy]|Static type checker|
|[typeguard]|Type checking for functions|
|[MkDocs]|Project documentation|
|[mkdocstrings]|Automatic documentation|
|[isort]|Sort imports and separate them into sections and types|

and the packages to build the project are

|package|description|
|:-----|:-----------------|
|[typer]|Command line interface|
|[requests]|HTTP library for Python|
|[prefect]|Manage the dataflow|
|[pandas]|Data analysis and manipulaiton tool|
|[numpy]|Scientific computing|
|[pyodbc]|Access ODBC database|
|[SQLAlchemy]|SQL toolkit and object relational mapper|

## Acknowledgements

The overall choices of packages is inspired from [hypermodern Python cookiecutter](https://cookiecutter-hypermodern-python.readthedocs.io/en/2020.6.15/index.html).

This data science project template is inspired from
[cookiecutter-modern-datascience](https://github.com/crmne/cookiecutter-modern-datascience)
for the directory structure.

The cookiecutter [data-science-tamplate](https://github.com/khuyentran1401/data-science-template) by
Khuyen Tran was also very much used.

## Quickstart

### Step 1 Setup the project structure with `cookiecutter`

Change to the parent location where you want the project to be created.
For example if your project is called `project-dsci` in the `parent` folder,
then move to `parent` first

    cd ../parent

verify that `cookiecutter` is properly installed by calling its version

    cookiecutter --version

then generate the project

    cookiecutter https://github.com/FrankLef/cookiecutter-dsci.git

and **make the new folder the working directory**.

### Step 2 Automate tasks with `Makefile`

`Make` will automate tasks. The Make file will be used repeatedly hereinafter to automate the tasks.

### Step 3 Manage the dependencies with `poetry`

* run `poetry shell` to open the poetry shell and avoid having to always add `poetry run`in front
of all commands and
* run `poetry update` so that the `poetry.lock` file will be created and the virtual environment
updated with the right packages and versions.

This is all encodedd in the `Makefile` so lets use it

    make poetry_start

It is a good idea to check poetry with `show`, it will raise an eror if there is any inconsistency.

    poetry show

Sometimes, especially when reusing a folder that had been used as a project before, the old environment
is still used. To delete it use this command

    poetry env remove <python>

run `poetry update` so that the `poetry.lock` file will be created and the virtual environment
updated with the right packages and versions.

### Step 4 Setup the new `.git`

First create the new repo in github

* Give the repo the exact same name as the project. That is keep the underscore in the name when there one. i.e. flproj_todo is also flproj_todo in github.
* Don't create `README`, `.gitignore` and `LICENSE` with the new repo they will be overriden anyway.

Then initialize git using

    make git_init

### Step 5 Install `pre-commit`

Once `.git` is setup, make sure to include the pre-commit script in `.git`
by running this command from the poetry shell

    poetry run pre-commit install

Sometimes warnings appear about the 'rev' field being mutable. Using this command
usually resolves this

    pre-commit autoupdate

It is also a good idea to run the hooks against all files when adding a new hook

    pre-commit run --all-files

### Step 6 Run `make lint`

To run `isort` and `flake8` and verify all is in order run this make command

    make lint

### Step 7 Create the documentation with `mkdocs`

You can also verify that the documentation setup is working by building the site with
this command

    mkdocs serve

which should give you something like this. Simply copy the http address to a browser address bar
to see the documentation site.

    INFO    -  Building documentation...
    INFO    -  Cleaning site directory
    INFO    -  Documentation built in 0.22 seconds
    [I 220510 0:0:0 server:335] Serving on http://127.0.0.1:8000
    INFO    -  Serving on http://127.0.0.1:8000

## Directory structure

This is how the new project will be organized.

    ├── .gitignore                <- GitHub's Python .gitignore customized for this project.
    ├── pre-commit-config.yaml    <- Settings for `pre-commit`.
    ├── LICENSE                   <- The project's license.
    ├── Makefile                  <- Scripts to automate tasks.
    ├── mkdocs.yaml               <- Settings for `mkdocs`.
    ├── noxfile.py                <- Sessions used by `nox`.
    ├── pyproject.toml            <- Configuration file used by `poetry`.
    ├── README.md                 <- The top-level README for developers using this project.
    ├── config                    <- Configuration files used by `hydra`.
    │   ├── main.yaml             <- Main configuration file.
    │   └── process               <- Configurations for data processing.
    │       ├── process01a.yaml   <- Config file.
    │       └── process02a.yaml   <- Config file.
    ├── data
    │   ├── 0_raw                 <- The original, immutable data dump.
    │   ├── 0_external            <- Data from third party sources.
    │   ├── 1_interim             <- Intermediate data that has been transformed.
    │   └── 2_final               <- The final, canonical data sets for modeling.
    ├── docs                      <- GitHub pages website.
    │   ├── explanation.md        <- Understanding-oriented documentation.
    │   ├── how-to-guides.md      <- Problem-oriented documentation.
    │   ├── index.md              <- The index page for the whole documentation.
    │   ├── reference.md          <- Information-oriented documentation.
    │   └── tutorials.md          <- Learning-oriented documentation.
    ├── notebooks                 <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                                the creator's initials, and a short `_` delimited description, e.g.
    │                                `01_fl_exploratory_data_analysis.ipynb`.
    ├── output
    │   ├── features              <- Fitted and serialized features.
    │   ├── models                <- Trained and serialized models, model predictions, or model summaries.
    │   └── reports               <- Generated analyses as HTML, PDF, LaTeX, etc.
    │       └── data              <- Generated graphics, figures, tables, etc. used in reporting.
    ├── src                       <- Store the source code.
    │   ├── process.py            <- The CLI entry point for all the processes/pipelines.
    │   └── process               <- Code for the various steps of the processes/pipelines.
    │       ├──  __init__.py
    │       ├── etl.py            <- Download, generate, and process data.
    │       ├── visualize.py      <- Create visualizations.
    │       ├── features.py       <- Turn raw data into features for modeling.
    │       └── train.py          <- Train and evaluate models.
    └── tests                 <- All test and fixtures files used by `pytest`.
        ├── fixtures          <- Where to put example inputs and outputs.
        │   ├── input.json    <- Test input data.
        │   └── output.json   <- Test output data.
        ├── test_etl          <- Test example on `etl.py`.
        └── test_samples.py   <- Test example to verify `pytest`.

[cookiecutter]: https://github.com/audreyr/cookiecutter
[poetry]: https://pypi.org/project/poetry/
[flake8]: https://pypi.org/project/flake8/
[pep8-naming]: https://pythonfix.com/pkg/p/pep8-naming/
[black]: https://pypi.org/project/black/
[pre-commit]: https://pypi.org/project/pre-commit/
[pre-commit-hooks]: https://github.com/pre-commit/pre-commit-hooks
[pytest]: https://pypi.org/project/pytest/
[mypy]: http://www.mypy-lang.org
[typeguard]: https://typeguard.readthedocs.io/en/latest/
[isort]: https://github.com/PyCQA/isort
[MkDocs]: https://www.mkdocs.org
[mkdocstrings]: https://mkdocstrings.github.io
[typer]: https://typer.tiangolo.com
[requests]: https://requests.readthedocs.io/en/latest/
[prefect]: https://docs.prefect.io
[pandas]: https://pandas.pydata.org
[numpy]: https://numpy.org
[pyodbc]: https://pypi.org/project/pyodbc/
[SQLAlchemy]: https://www.sqlalchemy.org
