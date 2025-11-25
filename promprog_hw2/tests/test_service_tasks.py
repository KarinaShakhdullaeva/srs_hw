from __future__ import annotations

import pytest

from app.domain.exceptions import NotFoundError
from app.dto.task import TaskCreate, TaskUpdate
from app.repositories.memory import InMemoryTaskRepository
from app.services.tasks_service import TaskService


def _new_service() -> TaskService:
    return TaskService(InMemoryTaskRepository())


def test_create_and_get_roundtrip() -> None:
    service = _new_service()
    created = service.create(TaskCreate(title="Read book"))
    got = service.get(created.id)
    assert got.title == "Read book"
    assert got.status == "todo"


def test_update_and_list_filters() -> None:
    service = _new_service()
    a = service.create(TaskCreate(title="A"))
    b = service.create(TaskCreate(title="B"))
    service.update(a.id, TaskUpdate(status="in_progress"))
    all_tasks = service.list()
    assert {t.id for t in all_tasks} == {a.id, b.id}
    only_in_progress = service.list(status="in_progress")
    assert [t.id for t in only_in_progress] == [a.id]


def test_delete_and_missing() -> None:
    service = _new_service()
    t = service.create(TaskCreate(title="Tmp"))
    service.delete(t.id)
    with pytest.raises(NotFoundError):
        _ = service.get(t.id)
    with pytest.raises(NotFoundError):
        service.delete(999)