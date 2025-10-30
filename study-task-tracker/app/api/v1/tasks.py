from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskRead
from app.domain.services import TaskService
from app.infrastructure.db import get_session
from app.infrastructure.repositories import TaskRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, session: Session = Depends(get_session)) -> TaskRead:
    service = TaskService(TaskRepository(session))
    created = service.create_task(payload)
    return created

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int, session: Session = Depends(get_session)) -> TaskRead:
    service = TaskService(TaskRepository(session))
    result = service.get_task(task_id)
    if result is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return result