import urllib
from pathlib import Path

import hydra
import pandas as pd
import sqlalchemy as sa
from omegaconf import DictConfig
from sqlalchemy.exc import SQLAlchemyError


def build_engine(path: str) -> sa.engine:
    """Create SQLAlchemy engine for MS Access.
    Args:
        path (str): Path to MS Access database.
    Returns:
        sa.engine: SQLAlchemy engine for MS Access.
    Raises:
        FileNotFoundError: The MS Access file name is invalid.
    """
    if Path(path).is_file() is False:
        msg = "\n" + path + "\nis an invalid MS Access DB file name."
        raise FileNotFoundError(msg)
    db_driver = "{Microsoft Access Driver (*.mdb, *.accdb)}"
    conn_str = f"DRIVER={db_driver};" f"DBQ={path};" "Mode=Read;"
    url_str = urllib.parse.quote_plus(conn_str)
    url_str = rf"access+pyodbc://?odbc_connect={url_str}"
    acc_engine = sa.create_engine(url_str)
    return acc_engine


def extract(tables: set[str], engine: sa.engine) -> dict:
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
        try:
            df = pd.read_sql(sql=sql_str, con=engine)
        except SQLAlchemyError as err:
            # https://stackoverflow.com/questions/2136739/error-handling-in-sqlalchemy
            # msg = str(err.__dict__["orig"])
            msg = str(err)
            msg = "THE ERROR:" + str(type(err))
            print(msg)
            raise
        out[tbl] = df
    engine.dispose()
    return out


@hydra.main(version_base=None, config_path="../../config/etl", config_name="db")
def main(cfg: DictConfig) -> dict:
    """Extract data from MS Access

    Args:
        cfg (DictConfig): Configuration using hydra.

    Returns:
        dict: Datasets from MS Access.
    """
    path = cfg.acc.path
    acc_engine = build_engine(path=path)
    tables = cfg.acc.tables
    raw_data = extract(tables=tables, engine=acc_engine)
    # print the shape of every table
    {tbl: print(df.shape) for (tbl, df) in raw_data.items()}
    return raw_data


if __name__ == "__main__":
    main()
