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
4. Сравнение типов данных до и после приведения

---

## Как запустить
   ```bash
   python data_loader.py
   ```

## Пример вывода 

<img width="1464" height="1077" alt="image" src="https://github.com/user-attachments/assets/d657b47c-310e-43e2-9ba0-a0686d49ee51" />
<img width="1092" height="1075" alt="image" src="https://github.com/user-attachments/assets/fdf2b511-4098-419d-ba58-7bcec69b7a35" />



