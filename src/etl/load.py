import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine, text
import sqlite3  # fallback, если нет PostgreSQL

def save_parquet(df: pd.DataFrame, path: str = "data/processed/processed_dataset.parquet") -> str:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    print(f"Сохранено в {path}")
    return path


def load_to_postgres(df: pd.DataFrame, creds_db: str = "creds.db", table_name: str = "topalova"):
    """
    Загружает до 100 строк в PostgreSQL, используя параметры из локальной creds.db.
    """
    import sqlite3
    conn = sqlite3.connect(creds_db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM access LIMIT 1;")
    row = [r for r in cur.fetchall()]
    cur.execute("PRAGMA table_info(access)")
    cols = [r for r in cur.fetchall()]
    conn.close()

    cols_transpose = [list(row) for row in zip(*cols)]
    data = dict(zip(cols_transpose[1], row[0]))

    db_user = data["user"]
    db_password = data["pass"]
    db_url = data["url"]
    db_port = data["port"]
    db_root_base = "homeworks"

    engine = create_engine(
        f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_root_base}"
    )

    df = df.head(100)
    df.to_sql(
        name=table_name,
        con=engine,
        schema="public",
        if_exists="replace",
        index=True,
    )

    with engine.begin() as conn:
        conn.execute(text(f'ALTER TABLE public.{table_name} ADD PRIMARY KEY (index)'))
    print(f"Данные загружены в таблицу public.{table_name} (до 100 строк).")
