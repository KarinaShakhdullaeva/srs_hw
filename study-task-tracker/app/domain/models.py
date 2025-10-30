from dataclasses import dataclass
from datetime import datetime, date, timezone
from enum import Enum
from typing import Optional

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

@dataclass(frozen=True)
class Task:
    id: Optional[int]
    title: str
    description: Optional[str]
    due_date: Optional[date]
    status: TaskStatus
    created_at: datetime

    @staticmethod
    def new(title: str, description: Optional[str], due_date: Optional[date]) -> "Task":
        return Task(
            id=None,
            title=title.strip(),
            description=description.strip() if description else None,
            due_date=due_date,
            status=TaskStatus.todo,
            created_at=datetime.now(tz=timezone.utc),
        )
