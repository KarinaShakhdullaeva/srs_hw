from fastapi import FastAPI
from app.api.v1.tasks import router as tasks_router
from app.observability import setup_logging

setup_logging()

app = FastAPI(title="Study Task Tracker", version="0.1.0")
app.include_router(tasks_router, prefix="/api/v1")