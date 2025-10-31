# Data Engineering Project 

Проект по автоматизированной загрузке, предварительной обработке и оптимизации датасета из Google Drive.  
Датасет содержит информацию о трендах на двух платформах: Тикток и Ютуб

[Ссылка на датасет](https://drive.google.com/file/d/1PLRMh5K3zbbXbN8HYnyciJWkfhosadFs/view?usp=drive_link)

## Описание данных
| Признак | Тип данных | Описание |
|----------|-------------|----------|
| platform | category | Платформа публикации |
| country | category | Страна публикации |
| views | int | Количество просмотров |
| ... | ... | ... |

[Полное описание признаков (CSV)](https://drive.google.com/file/d/1ikhqJXk4jEJRSeEyaxPqdkKiUk_0CCKW/view?usp=drive_link)

---
## Структура проекта
```
data_engineering/
├── src/
│   └── etl/                  # Основной ETL-пакет
│       ├── extract.py         # Загрузка исходных данных (из Google Drive и других источников)
│       ├── transform.py       # Очистка, преобразование и оптимизация типов данных
│       ├── load.py            # Загрузка обработанных данных в базу (PostgreSQL)
│       ├── validate.py        # Проверка корректности и структуры данных
│       └── main.py            # Объединение всех этапов ETL-пайплайна
│
├── experiments/               # Экспериментальные скрипты, ноутбуки, EDA
│
├── pyproject.toml             # Настройки зависимостей проекта (Poetry)
│
└── README.md                  # Описание проекта и инструкция по запуску

```
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



