# Sentiment Analyzer

## Цель проекта
Инструмент для автоматического анализа тональности текстов
(positive / negative / neutral) с возможностью batch-анализа,
оценки уверенности модели и получения истории анализов через API.

## Функциональность
- Очистка и нормализация текста
- Анализ тональности с confidence score
- Batch-анализ списков текстов
- Подсчёт статистики
- Хранение истории анализов (in-memory)
- REST API на FastAPI
- CLI-интерфейс
- Визуализация распределения тональностей

## Структура проекта
- src/ — исходный код
- tests/ — автоматические тесты
- data/ — примеры входных данных

## Установка
```bash
poetry install
```

## Запуск CLI
```bash
poetry run python src/sentiment_analyzer/main.py --input data/example_texts.csv
```

## Запуск API

(Нельзя добавлять перегрузку "--reload" в стабильную верисю. Это инструмент для разработки. Юзер должен использовать ваш 
сервис в production-режиме)
```bash
poetry run uvicorn sentiment_analyzer.api:app --reload
```

# Swagger:
```bash
http://127.0.0.1:8000/docs
```

## Архитектура проекта
```
sentiment_analyzer/
│
├── README.md
├── .gitignore
├── pyproject.toml
├── poetry.lock
├── src/  (`src` - это изоляция основного кода, а не модуль как таковой. Представьте, что src нет. Вы бы тоже положили все файлы вперемешку на 1 уровень или все-таки разделили бы по папкам?)
│   ├── __init__.py  (Не нужен. src - это не модуль)
│   ├── preprocessing.py
│   ├── model.py
│   ├── analyzer.py
│   ├── visualization.py
│   ├── cli.py
│   └── main.py
├── tests/
│   ├── test_preprocessing.py
│   ├── test_model.py
│   └── test_analyzer.py
└── data/
    └── example_texts.csv  (У вас не так :( )
```
### Основные компоненты

- preprocessing.py (Очистка и нормализация текста)
- model.py (TF-IDF + Logistic Regression, возвращает класс и confidence score)
- analyzer.py (Связывает предобработку и модель, формирует результаты и статистику.)
- storage.py (Xранилище batch-анализов)
- api.py (REST API (FastAPI) для анализа и получения истории.)
- cli.py, main.py (Запуск анализа из командной строки.)
