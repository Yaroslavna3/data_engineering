import pandas as pd

def validate(df: pd.DataFrame, max_rows: int = 100000) -> None:
    """
    Проверяет базовые ограничения:
    - не более max_rows строк
    - нет полностью пустых строк
    """
    if df.shape[0] == 0:
        raise ValueError("Датасет пуст.")
    if df.shape[0] > max_rows:
        raise ValueError(f"Датасет содержит {df.shape[0]} строк, лимит {max_rows}.")
    if df.isnull().all(axis=1).any():
        raise ValueError("Обнаружены полностью пустые строки.")

