import pytest
import sqlalchemy as sa
from hydra import compose, initialize

import src.process.etl as etl


@pytest.fixture
def acc_path():
    with initialize(version_base=None, config_path="../config/etl"):
        cfg = compose(config_name="db")
        return cfg.acc.path


def test_with_initialize() -> None:
    with initialize(version_base=None, config_path="../config/etl"):
        cfg = compose(config_name="db")
        target = r"C:\\Users\\Public\\MyJob\\DesjCap_cies\\PHT\\db_PHT_V1_xprt.accdb"
        assert cfg.acc.path == target
        # print(cfg.acc.tables)
        assert cfg.acc.tables == ["tbl_xprt_sales_grp", "tbl_xprt_part"]


def etl_engine(acc_path):
    out = etl.build_engine(acc_path)
    assert isinstance(out, sa.engine)


def test_etl_err():
    with pytest.raises(FileNotFoundError):
        etl.build_engine("wrong")
