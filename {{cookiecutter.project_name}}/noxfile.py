"""
Nox sessions.
Use nox_poetry to use pyproject.toml instead of requirements.txt.
"""

from nox_poetry import session


@session()
def tests(session):
    session.install("pytest")
    session.run("pytest")


@session()
def lint(session):
    session.install("isort")
    session.run("isort")
    session.install("flake8")
    session.run("flake8")
    # no need to call black if you call flake8 in nox
