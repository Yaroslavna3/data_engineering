import pandas as pd

FILE_ID = "1RRt9sN3xSrAoGq-4kGoO-AcTCTrZWqdq"  
file_url = f"https://drive.google.com/uc?id=1RRt9sN3xSrAoGq-4kGoO-AcTCTrZWqdq&export=download"

def main():
    try:
        response = requests.get(file_url)
        response.raise_for_status()  
                       
        raw_data = pd.read_csv(StringIO(response.text), sep=',')
        print("Первые 10 строк датасета:")
        print(raw_data.head(10))
    except Exception as e:
        print("Ошибка при загрузке:", e)

if __name__ == "__main__":
    main()
