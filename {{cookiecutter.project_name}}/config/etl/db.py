from pathlib import Path


def set_path(path: str) -> str:
    out = Path("C:/Users/Public/MyJob/DesjCap_cies/PHT/db_PHT_V1_xprt.accdb")
    if Path.exists(out) is False:
        raise FileNotFoundError("The database file name is invalid.")
    return out


def set_tables(tables=tuple[str, ...]) -> tuple[str, ...]:
    if len(tables) == 0:
        raise ValueError("There must be at least one table name.")
    msg = "There should be no duplicate table names."
    assert len(tables) == len(set(tables)), msg
    return tables


PATH = set_path(path="C:/Users/Public/MyJob/DesjCap_cies/PHT/db_PHT_V1_xprt.accdb")

TABLES = set_tables(("tbl_xprt_sales_grp", "tbl_xprt_part"))
