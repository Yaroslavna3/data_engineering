import requests
import pandas as pd

def get_cat_facts(limit=5):
    print("➡️ Запрашиваем данные с API...")
    url = f"https://catfact.ninja/facts?limit={limit}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print("❌ Ошибка при запросе:", e)
        return None

    print("✅ Ответ получен, обрабатываем данные...")
    data = response.json().get("data", [])
    
    if not data:
        print("⚠️ API вернул пустой ответ!")
        return None
    
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    print("🚀 Скрипт запущен")
    df = get_cat_facts(10)
    
    if df is not None:
        print("\n📋 Первые строки данных:")
        print(df.head())
        df.to_csv("cat_facts.csv", index=False)
        print("\n💾 Данные сохранены в cat_facts.csv")
    else:
        print("❗ Не удалось получить данные от API.")
