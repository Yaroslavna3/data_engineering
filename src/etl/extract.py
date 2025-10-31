import gdown
import pandas as pd
from pathlib import Path

def extract_from_gdrive(file_id: str, output_dir: str = "data/raw") -> pd.DataFrame:
    """
    Загружает CSV с Google Drive и возвращает DataFrame.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    file_url = f"https://drive.google.com/uc?id={file_id}"
    output_path = Path(output_dir) / "dataset.csv"

    print(f"Скачиваю файл из Google Drive ({file_id})...")
    gdown.download(file_url, str(output_path), quiet=False)

    df = pd.read_csv(output_path)
    print(f"Загружено {len(df)} строк.")
    return df
