## Структура проекта

```
study-task-tracker-quality
│
├── app/
│   ├── api/              # HTTP-роуты FastAPI
│   ├── domain/           # доменные модели и исключения
│   ├── dto/              # Pydantic-схемы (вход/выход API)
│   ├── repositories/     # in-memory репозиторий задач
│   ├── services/         # бизнес-логика
│   └── main.py           # создание приложения и DI
│
├── tests/                # unit и API тесты (pytest)
│
└── docs/                 # скриншоты:
        allure-report.png
        coverage.png
        mypy-success.png
        pre-commit-success.png
```

---

##  Установка и запуск



```powershell
python -m venv .venv
.\.venv\Scripts\activate
```



```powershell
pip install -U pip
pip install -e .[dev]
```



```powershell
uvicorn app.main:app --reload
```

Документация API :  
http://127.0.0.1:8000/docs

---

##  Тесты и покрытие

В проекте используются:

- `pytest`
- `pytest-cov` 

Запуск:

```powershell
pytest
```

Полученный скриншот покрытия сохранён в:

```
docs/coverage.png
```

---

## Allure отчёт

1. Генерация результатов:

```powershell
pytest --alluredir=allure-results
```

2. Просмотр отчёта:

```powershell
allure serve allure-results
```

Скриншот интерфейса Allure расположен в:

```
docs/allure-report.png
```

---

## Статическая типизация (mypy)



Проверка:

```powershell
mypy .
```

Скриншот успешной проверки:

```
docs/mypy-success.png
```

---

## Линтеры и форматирование

Используются инструменты:

- **ruff** - линтер и проверки стиля
- **black** - форматирование
- **isort** - сортировка импортов

Команды:

```powershell
ruff check .
black .
isort .
```

---

## Pre-commit

Настроены хуки:

- на `pre-commit`: ruff, black, isort, mypy
- на `pre-push`: pytest

Установка:

```powershell
pre-commit install --hook-type pre-commit --hook-type pre-push
```

Проверка при коммите:

```powershell
git add .
git commit -m "test"
```

Скриншот успешного прогона хуков:

```
docs/pre-commit-success.png
```

---

## Пример команд для разработки

| Цель                     | Команда                                  |
|--------------------------|-------------------------------------------|
| Запуск тестов            | `pytest`                                 |
| Проверка покрытия        | `pytest --cov=app`                       |
| Статическая типизация    | `mypy .`                                 |
| Запуск линтеров          | `ruff check .`                           |
| Автоформатирование       | `black . && isort .`                     |
| Запуск приложения        | `uvicorn app.main:app --reload`          |

---