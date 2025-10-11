import pandas as pd
import gdown

FILE_ID = "1PLRMh5K3zbbXbN8HYnyciJWkfhosadFs"  
file_url = f"https://drive.google.com/uc?id=1PLRMh5K3zbbXbN8HYnyciJWkfhosadFs"

def main():
    try:
        output = "dataset.csv"
        gdown.download(file_url, output, quiet=False)

        raw_data = pd.read_csv(output)
        print("Первые 10 строк датасета:")
        print(raw_data.head(10))
        
        # --- Автоматическое приведение типов ---
        # Категориальные 
        cat_cols = [
            "platform", "country", "region", "language", "category", "hashtag",
            "title_keywords", "author_handle", "sound_type", "music_track",
            "trend_label", "source_hint", "notes", "device_type", "genre",
            "trend_type", "publish_dayofweek", "publish_period", "event_season",
            "tags", "sample_comments", "creator_tier", "season",
            "device_brand", "traffic_source"
        ]
        for col in cat_cols:
            if col in raw_data.columns:
                raw_data[col] = raw_data[col].astype("category")

        # Даты
        date_cols = ["publish_date_approx", "year_month"]
        for col in date_cols:
            if col in raw_data.columns:
                raw_data[col] = pd.to_datetime(raw_data[col], errors="coerce")

        # Числовые
        for col in raw_data.select_dtypes(include="int64").columns:
            raw_data[col] = pd.to_numeric(raw_data[col], downcast="integer")
        for col in raw_data.select_dtypes(include="float64").columns:
            raw_data[col] = pd.to_numeric(raw_data[col], downcast="float")

        # --- Сохраняем результат ---
        processed_output = "processed_dataset.parquet"
        raw_data.to_parquet(processed_output, index=False)

        print(f"Датасет приведён к оптимальным типам и сохранён в {processed_output}")
        
    except Exception as e:
        print("Ошибка при загрузке:", e)

if __name__ == "__main__":
    main()
