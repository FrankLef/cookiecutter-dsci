from pathlib import Path

import pytest
import config.main as cfg_main
import config.etl.db as cfg_db


@pytest.fixture
def cwd_path():
    return cfg_main.CWD_PATH


@pytest.fixture
def db_path():
    return cfg_db.PATH


@pytest.fixture
def db_tables():
    return cfg_db.TABLES


def test_cwd_path(cwd_path):
    assert Path(cwd_path).is_dir()
    assert cwd_path == Path.cwd()


def test_db_path(db_path):
    assert Path.exists(db_path)
    assert db_path == Path(
        'C:/Users/Public/MyJob/DesjCap_cies/PHT/db_PHT_V1_xprt.accdb')


def test_db_tables(db_tables):
    assert db_tables == ('tbl_xprt_sales_grp', 'tbl_xprt_part')
