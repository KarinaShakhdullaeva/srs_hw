from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Literal

Status = Literal["todo", "in_progress", "done"]


@dataclass(slots=True)
class Task:
    id: int
    title: str
    description: str | None
    status: Status
    due_date: date | None
    created_at: datetime