from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.infrastructure.repositories import TaskRepository
from app.domain.models import Task
from app.schemas.task import TaskCreate
from app.domain.services import TaskService

def test_create_and_get_task_service():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, future=True)
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
    session = SessionLocal()

    repo = TaskRepository(session)
    service = TaskService(repo)

    created = service.create_task(TaskCreate(title="Read chapter 1", description="Math", due_date=None))
    assert created.id is not None
    assert created.title == "Read chapter 1"
    fetched = service.get_task(created.id)
    assert fetched is not None
    assert fetched.id == created.id
