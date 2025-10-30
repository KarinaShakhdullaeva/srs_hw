from datetime import datetime, date
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, Date, DateTime

from app.domain.models import Task as DomainTask, TaskStatus

class Base(DeclarativeBase):
    pass

class TaskORM(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    due_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(String(32), nullable=False, default=TaskStatus.todo.value)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    def to_domain(self) -> DomainTask:
        return DomainTask(
            id=self.id,
            title=self.title,
            description=self.description,
            due_date=self.due_date,
            status=TaskStatus(self.status),
            created_at=self.created_at,
        )

    @staticmethod
    def from_domain(task: DomainTask) -> "TaskORM":
        orm = TaskORM(
            title=task.title,
            description=task.description,
            due_date=task.due_date,
            status=task.status.value,
            created_at=task.created_at,
        )
        # id проставится автоматически при insert
        return orm