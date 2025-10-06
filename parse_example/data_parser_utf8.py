
import pandas as pd

def parse_remote_dataset():
    """
    Загружает публичный CSV-датаcет и выводит сводную информацию.
    Датасет не сохраняется в проекте.
    """
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"  # пример датасета

    print("📥 Загружаем датасет...")
    df = pd.read_csv(url)
    print("✅ Датасет успешно загружен!\n")

    print("📊 Первые строки данных:")
    print(df.head(), "\n")

    print("ℹ️ Информация о данных:")
    print(df.info(), "\n")

    print("📈 Описательная статистика:")
    print(df.describe())

if __name__ == "__main__":
    parse_remote_dataset()