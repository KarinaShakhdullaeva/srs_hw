from __future__ import annotations

from datetime import date, datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Status = Literal["todo", "in_progress", "done"]


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    due_date: date | None = None


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    status: Status | None = None
    due_date: date | None = None


class TaskRead(BaseModel):
    id: int
    title: str
    description: str | None
    status: Status
    due_date: date | None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)
