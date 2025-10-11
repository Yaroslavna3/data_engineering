# Data Engineering Project 

Проект по автоматизированной загрузке, предварительной обработке и оптимизации датасета из Google Drive.  
Код написан на **Python** 

[link on data set](https://drive.google.com/drive/folders/1RRt9sN3xSrAoGq-4kGoO-AcTCTrZWqdq?usp=sharing)

---

## Основной скрипт

**Файл:** `data_loader.py`  
Скрипт выполняет:
1. Загрузку CSV-файла с Google Drive.
2. Автоматическое приведение типов данных (категориальные, числовые, даты).
3. Сохранение результата в формат `.parquet` для более эффективного хранения и анализа.

---

## Как запустить
   ```bash
   python data_loader.py
   ```

## Пример вывода 

<img width="1463" height="507" alt="image" src="https://github.com/user-attachments/assets/88f6b928-c23b-4edd-86c5-49d099e3e90d" />

