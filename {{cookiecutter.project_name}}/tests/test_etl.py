import pytest
import sqlalchemy as sa

from config import settings
import src.process.etl as etl


@pytest.fixture
def db_path():
    return settings.msaccess.path


@pytest.fixture
def db_tables():
    return settings.msaccess.tables


def test_etl_engine(db_path):
    out = etl.build_engine(db_path)
    assert isinstance(out, sa.engine.base.Engine)


def test_etl_err():
    with pytest.raises(FileNotFoundError):
        etl.build_engine("wrong path")
