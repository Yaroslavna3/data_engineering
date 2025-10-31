
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_quotes():
    
    url = "https://quotes.toscrape.com/"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes_data = []

    # Находим все блоки с цитатами
    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").get_text(strip=True)
        author = quote.find("small", class_="author").get_text(strip=True)
        tags = [tag.get_text(strip=True) for tag in quote.find_all("a", class_="tag")]

        quotes_data.append({
            "text": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    # Преобразуем в DataFrame
    df = pd.DataFrame(quotes_data)
    print("Найдено цитат:", len(df))
    print(df.head(), "\n")

    # Вывод результатов
    df.to_csv("quotes_output.csv", index=False)
    print("Результат сохранён в quotes_output.csv")

if __name__ == "__main__":
    scrape_quotes()
