from __future__ import annotations

from collections.abc import Iterable
from dataclasses import replace
from datetime import date
from typing import Any

from ..domain.exceptions import NotFoundError
from ..domain.models import Status, Task


class InMemoryTaskRepository:
    def __init__(self) -> None:
        self._items: dict[int, Task] = {}
        self._seq: int = 0

    def _next_id(self) -> int:
        self._seq += 1
        return self._seq

    def add(self, task: Task) -> Task:
        if task.id in self._items:
            raise ValueError(f"Task with id={task.id} already exists")
        self._items[task.id] = task
        return task

    def create(
        self,
        *,
        title: str,
        description: str | None,
        status: Status,
        due_date: date | None,
    ) -> Task:
        from datetime import datetime

        task = Task(
            id=self._next_id(),
            title=title,
            description=description,
            status=status,
            due_date=due_date,
            created_at=datetime.utcnow(),
        )
        self._items[task.id] = task
        return task

    def get(self, task_id: int) -> Task:
        try:
            return self._items[task_id]
        except KeyError as exc:
            raise NotFoundError(f"Task id={task_id} not found") from exc

    def list(self, *, status: Status | None = None) -> list[Task]:
        items: Iterable[Task] = self._items.values()
        if status is not None:
            items = [t for t in items if t.status == status]
        return list(items)

    def update(self, task_id: int, **changes: Any) -> Task:
        task = self.get(task_id)
        updated = replace(task, **changes)
        self._items[task_id] = updated
        return updated

    def delete(self, task_id: int) -> None:
        if task_id not in self._items:
            raise NotFoundError(f"Task id={task_id} not found")
        del self._items[task_id]

    def clear(self) -> None:
        self._items.clear()
        self._seq = 0