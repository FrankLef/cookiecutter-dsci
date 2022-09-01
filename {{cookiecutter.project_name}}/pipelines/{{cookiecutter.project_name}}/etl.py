import urllib

import pandas as pd
import sqlalchemy as sa


def build_engine(path: str) -> sa.engine:
    """Create SQLAlchemy engine for MS Access.

    Args:
        path (str): Path to MS Access database.

    Returns:
        sa.engine: SQLAlchemy engine for MS Access.
    """
    db_driver = "{Microsoft Access Driver (*.mdb, *.accdb)}"
    db_path = path
    conn_str = rf"DRIVER={db_driver};" rf"DBQ={db_path};" r"Mode=Read;"
    url_str = urllib.parse.quote_plus(conn_str)
    url_str = rf"access+pyodbc://?odbc_connect={url_str}"
    acc_engine = sa.create_engine(url_str)
    return acc_engine


def extract_acc(tables: set[str], engine: sa.engine) -> dict:
    """Extract data from MS Access.

    Args:
        tables (set[str]): Names of tables.
        engine (sa.engine): SQLAlchemy engine for MS Access.

    Returns:
        dict: Datasets from MS Access.
    """
    out = {}
    for tbl in tables:
        sql_str = "select * from " + tbl
        df = pd.read_sql(sql=sql_str, con=engine)
        out[tbl] = df
    engine.dispose()
    return out


def main():
    # MANUAL ENTRY
    path_str = r"C:\Users\Public\MyJob\DesjCap_cies\PHT\db_PHT_V1_xprt.accdb"
    acc_engine = build_engine(path=path_str)
    # MANUAL ENTRY
    the_tables = {"tbl_xprt_sales_grp", "tbl_xprt_part"}
    raw_data = extract_acc(tables=the_tables, engine=acc_engine)
    # print the shape of every table
    {tbl: print(df.shape) for (tbl, df) in raw_data.items()}
    return raw_data


if __name__ == "__main__":
    main()
