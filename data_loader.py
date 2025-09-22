import pandas as pd
import gdown

FILE_ID = "1RRt9sN3xSrAoGq-4kGoO-AcTCTrZWqdq"  
file_url = f"https://drive.google.com/uc?id=1RRt9sN3xSrAoGq-4kGoO-AcTCTrZWqdq"

def main():
    try:
        output = "dataset.csv"
        gdown.download(file_url, output, quiet=False)

       raw_data = pd.read_csv(output)
        print("Первые 10 строк датасета:")
        print(raw_data.head(10))
    except Exception as e:
        print("Ошибка при загрузке:", e)

if __name__ == "__main__":
    main()
