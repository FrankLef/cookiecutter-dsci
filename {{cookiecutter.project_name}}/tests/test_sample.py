# This is a sample file to validate pytest and nox.
# It can be deleted.

from pytest import raises


def func(x, y):
    return x + y


def test_answer():
    assert func(1, 2) == 3


def f():
    raise SystemExit(1)


def test_mytest():
    with raises(SystemExit):
        f()
