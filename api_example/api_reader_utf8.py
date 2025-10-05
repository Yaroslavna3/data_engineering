import requests
import pandas as pd

def get_cat_facts(limit=5):
    
    url = f"https://catfact.ninja/facts?limit={limit}"
    response = requests.get(url)
    response.raise_for_status()  

    data = response.json()["data"]
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    df = get_cat_facts(10)
    print(df.head())  
    df.to_csv("cat_facts.csv", index=False)
    print("\nДанные сохранены в cat_facts.csv")
