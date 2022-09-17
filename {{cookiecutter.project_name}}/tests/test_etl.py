import pytest

import src.etl as etl


@pytest.fixture
def acc_info():
    out = [
        r"C:\Users\Public\MyJob\DesjCap_cies\PHT\db_PHT_V1_xprt.accdb",
        {"tbl_xprt_sales_grp", "tbl_xprt_part"},
    ]
    return out


def test_etl(acc_info):
    out = etl.main(path=acc_info[0], tables=acc_info[1])
    assert isinstance(out, dict)
    assert len(out) == len(acc_info)


def test_etl_err(acc_info):
    with pytest.raises(FileNotFoundError):
        etl.main(path="WRONG", tables=acc_info[1])
