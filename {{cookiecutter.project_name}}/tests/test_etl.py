import pytest
import sqlalchemy as sa
import config.etl.db as cfg
import src.process.etl as etl


@pytest.fixture
def db_path():
    return cfg.PATH


@pytest.fixture
def db_tables():
    return cfg.TABLES


def test_etl_engine(db_path):
    out = etl.build_engine(db_path)
    assert isinstance(out, sa.engine.base.Engine)


def test_etl_err():
    with pytest.raises(FileNotFoundError):
        etl.build_engine("wrong path")
