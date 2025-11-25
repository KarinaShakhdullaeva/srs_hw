from __future__ import annotations

from fastapi import APIRouter, Depends, FastAPI, HTTPException, Request, status

from ..domain.exceptions import NotFoundError
from ..domain.models import Status
from ..dto.task import TaskCreate, TaskRead, TaskUpdate
from ..services.tasks_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_service() -> TaskService:
    from ..main import task_service

    return task_service


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
def create_task(
    data: TaskCreate,
    service: TaskService = Depends(get_service),  # noqa: B008
) -> TaskRead:
    return service.create(data)


@router.get("/{task_id}", response_model=TaskRead)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_service),  # noqa: B008
) -> TaskRead:
    return service.get(task_id)


@router.get("", response_model=list[TaskRead])
def list_tasks(
    status: Status | None = None,
    service: TaskService = Depends(get_service),  # noqa: B008
) -> list[TaskRead]:
    return service.list(status=status)


@router.put("/{task_id}", response_model=TaskRead)
def update_task(
    task_id: int,
    data: TaskUpdate,
    service: TaskService = Depends(get_service),  # noqa: B008
) -> TaskRead:
    return service.update(task_id, data)


@router.delete("/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_service),  # noqa: B008
) -> dict:
    service.delete(task_id)
    return {"ok": True}


def install_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(NotFoundError)
    async def _not_found_handler(request: Request, exc: NotFoundError) -> None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )