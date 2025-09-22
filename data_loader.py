import pandas as pd

FILE_ID = "1RRt9sN3xSrAoGq-4kGoO-AcTCTrZWqdq"  
file_url = f"https://drive.google.com/drive/folders/1RRt9sN3xSrAoGq-4kGoO-AcTCTrZWqdq"

def main():
    raw_data = pd.read_csv(file_url)
    print("Первые 10 строк датасета:")
    print(raw_data.head(10))

if __name__ == "__main__":
    main()
