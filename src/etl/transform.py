import pandas as pd

def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Приводит типы данных к оптимальным форматам (категориальные, даты, числа).
    """
    cat_cols = [
        "platform", "country", "region", "language", "category", "hashtag",
        "title_keywords", "author_handle", "sound_type", "music_track",
        "trend_label", "source_hint", "notes", "device_type", "genre",
        "trend_type", "publish_dayofweek", "publish_period", "event_season",
        "tags", "sample_comments", "creator_tier", "season",
        "device_brand", "traffic_source"
    ]
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].astype("category")

    date_cols = ["publish_date_approx", "year_month"]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    for col in df.select_dtypes(include="int64").columns:
        df[col] = pd.to_numeric(df[col], downcast="integer")
    for col in df.select_dtypes(include="float64").columns:
        df[col] = pd.to_numeric(df[col], downcast="float")

    return df
