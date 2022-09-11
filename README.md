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
|[nox]|Task automation|
|[nox-poetry]|Enable `session.install` to use the Poetry lock file|

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

This data science project template is heavily inspired from
[cookiecutter-modern-datascience](https://github.com/crmne/cookiecutter-modern-datascience)
for the directory structure.

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

### Step 2 Manage the dependencies with `poetry`

The first thing to do is to open the poetry shell to avoid having to always add `poetry run` in front of all commands.

    poetry shell

then run `poetry update` so that the `poetry.lock` file will be created and the virtual environment
updated with the right packages and versions.

    poetry update

To add or remove from the `pyproject.toml` file **you must use the `add` and `remove` commands from `poetry`**.
**Don't do it manually**, otherwise the dependencies are not resolved and errors will probably be raised when doing
the `show` command.

It is a good idea to check poetry with `show`, it will raise an eror if there is any inconsistency.

    poetry show

Sometimes, especially when reusing a folder that had been used as a project before, the old environment
is still used. To delete it use this command

    poetry env remove <python>

### Step 3 Automate tasks with `nox`

`nox` will automate tasks. A task for linting has been created and can be used to test the nox install
as follows.

    nox --session lint

also the list of nox sessions availbale can be obtained with

    nox --list

**Important**: There is no `tests` section in the `noxfile.py` used for project as

* it creates a wheel which takes a long time and is not necessary
* changes the name of the project and insert an hyphen
* requires an `src` folder and to change the structure
* **it's a lot of problems!**

### Step 4 Setup the new `.git`

First create the new repo in github

* Don't forget the hyphen instead of the underscore in the name. i.e. flproj_todo becomes flproj-todo in github.
* Don't create `README`, `.gitignore` and `LICENSE` with the new repo they will be overriden anyway.

Then run the git commands

    git init
    git add --all
    git commit -m "initialize"
    git branch -M main
    git remote add origin https://github.com/FrankLef/flproj-todo.git
    # -u switch makes the remote repo the default for theexisting project
    # -f switch forces Git to overwrite anyfile that already exist on GitHub
    git push -u -f origin main

### Step 5 Install `pre-commit`

Once `.git` is setup, make sure to include the pre-commit script in `.git`
by running this command from the poetry shell

    poetry run pre-commit install

Sometimes warnings appear about the 'rev' field being mutable. Using this command
usually resolves this

    pre-commit autoupdate

It is also a good idea to run the hooks against all files when adding a new hook

    pre-commit run --all-files

### Step 6 Create the documentation with `mkdocs`

You can also verify that the documentation setup is working by building the site with
this command

    mkdocs serve

which should give you something like this. Simply copy the http address to a browser address bar 
to see the documentation site.

```shell
INFO    -  Building documentation...
INFO    -  Cleaning site directory
INFO    -  Documentation built in 0.22 seconds
[I 220510 0:0:0 server:335] Serving on http://127.0.0.1:8000
INFO    -  Serving on http://127.0.0.1:8000
```



## Directory structure

This is how the new project will be organized.

    ├── .gitignore                <- GitHub's excellent Python .gitignore customized for this project.
    ├── pre-commit-config.yaml    <- Settings for `pre-commit`.
    ├── LICENSE                   <- The project's license.
    ├── mkdocs.yml                <- Settings for `mkdocs`.
    ├── noxfile.py                <- Functions used by `nox`.
    ├── pyproject.toml            <- The pyproject file used by `poetry` to manage the environment.
    ├── README.md                 <- The top-level README for developers using this project.
    │
    ├── data
    │   ├── 0_raw                 <- The original, immutable data dump.
    │   ├── 0_external            <- Data from third party sources.
    │   ├── 1_interim             <- Intermediate data that has been transformed.
    │   └── 2_final               <- The final, canonical data sets for modeling.
    │
    ├── docs                      <- GitHub pages website.
    │   ├── explanation.md        <- Understanding-oriented documentation.
    │   ├── how-to-guides.md      <- Problem-oriented documentation.
    │   ├── index.md              <- The index page for the whole documentation.
    │   ├── reference.md          <- Information-oriented documentation.
    │   └── tutorials.md          <- Learning-oriented documentation.
    │
    ├── notebooks                 <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                                the creator's initials, and a short `_` delimited description, e.g.
    │                                `01_fl_exploratory_data_analysis.ipynb`.
    │
    ├── output
    │   ├── features              <- Fitted and serialized features.
    │   ├── models                <- Trained and serialized models, model predictions, or model summaries.
    │   └── reports               <- Generated analyses as HTML, PDF, LaTeX, etc.
    │       └── data              <- Generated graphics, figures, tables, etc. to be used in reporting.
    │
    ├── pipelines                 <- Pipelines and data workflows.
        ├── pipelines.py          <- The CLI entry point for all the pipelines.
        ├── <project_name>        <- Code for the various steps of the pipelines.
        │   ├──  __init__.py
        │   ├── etl.py            <- Download, generate, and process data.
        │   ├── visualize.py      <- Create exploratory and results oriented visualizations.
        │   ├── features.py       <- Turn raw data into features for modeling.
        │   └── train.py          <- Train and evaluate models.
        └── tests
            ├── fixtures          <- Where to put example inputs and outputs.
            │   ├── input.json    <- Test input data.
            │   └── output.json   <- Test output data.
            └── test_samples.py   <- Test example to verify `pytest`.

[cookiecutter]: https://github.com/audreyr/cookiecutter
[poetry]: https://pypi.org/project/poetry/
[nox]: https://nox.thea.codes/en/stable/
[nox-poetry]: https://github.com/cjolowicz/nox-poetry
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
