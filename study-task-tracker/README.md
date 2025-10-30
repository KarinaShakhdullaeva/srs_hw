# Study Task Tracker (FastAPI)

Простое приложение позволяет создавать и просматривать учебные задачи.

## Возможности
- Создать задачу (`POST /api/v1/tasks`)
- Получить задачу по ID (`GET /api/v1/tasks/{id}`)

## Запуск проекта

### Вариант 1: Локально (Windows / Linux / WSL)

#### Windows PowerShell
```powershell
py -3.11 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
uvicorn app.main:app --reload
```

#### Linux / WSL
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
uvicorn app.main:app --reload
```

После запуска в браузере:  
http://localhost:8000/docs

### Вариант 2: В контейнере (Docker)

```bash
docker build -t study-task-tracker .
docker run --rm -p 8000:8000 study-task-tracker
```

## Тесты

```bash
python -m pytest -q
```

## Структура

```
app/
  api/v1/tasks.py        # API слой (FastAPI router)
  domain/models.py       # Доменные сущности (dataclass + Enum)
  domain/services.py     # Бизнес-логика (Application service)
  infrastructure/db.py   # Инициализация БД, сессии
  infrastructure/orm.py  # ORM-модель SQLAlchemy
  infrastructure/repositories.py  # Репозитории
  schemas/task.py        # Pydantic-схемы (DTO)
  main.py                # Инициализация FastAPI
  observability.py       # Логирование и каркас метрик
tests/
  test_services.py
  test_api.py
diagrams/
  c4_container.png
  c4_component.png
```

## Проверка
1. Установить зависимости и запустить `uvicorn app.main:app --reload`.  
2. Перейти на `http://localhost:8000/docs` и создать задачу.