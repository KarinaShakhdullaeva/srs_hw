from __future__ import annotations

from fastapi import FastAPI

from .api import tasks as tasks_api
from .repositories.memory import InMemoryTaskRepository
from .services.tasks_service import TaskService

app = FastAPI(title="Study Task Tracker", version="0.2.0")

repo = InMemoryTaskRepository()
self_service = TaskService(repo)

task_service = self_service

tasks_api.install_exception_handlers(app)
app.include_router(tasks_api.router)


@app.get("/healthz", tags=["meta"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
