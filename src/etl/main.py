import argparse
from .extract import extract_from_gdrive
from .transform import optimize_dtypes
from .validate import validate
from .load import save_parquet, load_to_postgres

def run_etl(file_id: str):
    print("Запуск ETL-пайплайна...")
    df = extract_from_gdrive(file_id)
    df = optimize_dtypes(df)
    validate(df)
    save_parquet(df)
    # load_to_postgres(df)
    print("Пропущена загрузка в базу (демо-режим).")
    print("ETL успешно завершён!")

def cli():
    parser = argparse.ArgumentParser(description="ETL pipeline runner")
    parser.add_argument("--source-id", required=True, help="Google Drive file ID")
    args = parser.parse_args()
    run_etl(args.source_id)

if __name__ == "__main__":
    cli()

