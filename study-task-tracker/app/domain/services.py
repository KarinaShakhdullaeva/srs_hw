import logging
from typing import Optional

from app.schemas.task import TaskCreate, TaskRead
from app.domain.models import Task
from app.infrastructure.repositories import TaskRepository

logger = logging.getLogger(__name__)

class TaskService:
    def __init__(self, repo: TaskRepository) -> None:
        self.repo = repo

    def create_task(self, dto: TaskCreate) -> TaskRead:
        logger.info("Creating task with title=%s", dto.title) 
        domain_obj = Task.new(title=dto.title, description=dto.description, due_date=dto.due_date)
        saved = self.repo.add(domain_obj)
        return TaskRead.from_domain(saved)

    def get_task(self, task_id: int) -> Optional[TaskRead]:
        found = self.repo.get(task_id)
        return TaskRead.from_domain(found) if found else None
