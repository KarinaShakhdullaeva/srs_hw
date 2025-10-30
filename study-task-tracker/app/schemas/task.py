from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.domain.models import Task as DomainTask, TaskStatus

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=5000)
    due_date: Optional[date] = None

class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[date] = None
    status: TaskStatus
    created_at: datetime

    @staticmethod
    def from_domain(d: DomainTask) -> "TaskRead":
        return TaskRead(
            id=d.id,
            title=d.title,
            description=d.description,
            due_date=d.due_date,
            status=d.status,
            created_at=d.created_at,
        )