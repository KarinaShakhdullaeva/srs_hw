from __future__ import annotations

from ..domain.models import Status
from ..dto.task import TaskCreate, TaskRead, TaskUpdate
from ..repositories.memory import InMemoryTaskRepository


class TaskService:
    def __init__(self, repo: InMemoryTaskRepository) -> None:
        self._repo = repo

    def create(self, data: TaskCreate) -> TaskRead:
        task = self._repo.create(
            title=data.title,
            description=data.description,
            status="todo",
            due_date=data.due_date,
        )
        return TaskRead.model_validate(task)

    def get(self, task_id: int) -> TaskRead:
        task = self._repo.get(task_id)
        return TaskRead.model_validate(task)

    def list(self, *, status: Status | None = None) -> list[TaskRead]:
        tasks = self._repo.list(status=status)
        return [TaskRead.model_validate(t) for t in tasks]

    def update(self, task_id: int, data: TaskUpdate) -> TaskRead:
        if data.title == "":
            raise ValueError()
        changes = {
            key: value
            for key, value in data.model_dump(exclude_unset=True).items()
            if value is not None
        }
        updated = self._repo.update(task_id, **changes)
        return TaskRead.model_validate(updated)

    def delete(self, task_id: int) -> None:
        self._repo.delete(task_id)
