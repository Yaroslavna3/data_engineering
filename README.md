# Data Engineering Project 

Проект по автоматизированной загрузке, предварительной обработке и оптимизации датасета из Google Drive.  
Датасет содержит информацию о трендах на двух платформах: Тикток и Ютуб

[Ссылка на датасет](https://drive.google.com/drive/folders/1RRt9sN3xSrAoGq-4kGoO-AcTCTrZWqdq?usp=sharing)

## Описание данных
| Признак | Тип данных | Описание |
|----------|-------------|----------|
| platform | category | Платформа публикации |
| country | category | Страна публикации |
| views | int | Количество просмотров |
| ... | ... | ... |

[Полное описание признаков (CSV)]([experiments/feature_description.csv](https://drive.google.com/file/d/1ikhqJXk4jEJRSeEyaxPqdkKiUk_0CCKW/view?usp=drive_link))

---

## Настройка окружения
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/Yaroslavna3/data_engineering.git
   cd data_engineering
2. Установить зависимости
   ``` bash
   poetry install
---

## Как запустить
   ```bash
   python src/etl/main.py --source-id 1PLRMh5K3zbbXbN8HYnyciJWkfhosadFs

   ```
## Просмотреть EDA

Вы можете просмотреть рендер ноутбука через nbviewer:

[Открыть EDA-ноутбук в nbviewer](https://nbviewer.org/github/Yaroslavna3/data_engineering/blob/main/experiments/EDA.ipynb)



