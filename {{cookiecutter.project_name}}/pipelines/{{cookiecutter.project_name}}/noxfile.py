"""
Nox sessions.
Use nox_poetry to use pyproject.toml instead of requirements.txt.
"""

from nox_poetry import session


@session()
def tests(session):
    session.install("pytest")
    session.run("pytest")
