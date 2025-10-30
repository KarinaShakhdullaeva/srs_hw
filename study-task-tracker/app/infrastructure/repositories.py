from typing import Optional

from sqlalchemy.orm import Session

from app.infrastructure.orm import TaskORM, Base
from app.domain.models import Task as DomainTask

class TaskRepository:
    def __init__(self, session: Session) -> None:
        self.session = session
        Base.metadata.create_all(bind=self.session.get_bind())

    def add(self, task: DomainTask) -> DomainTask:
        orm = TaskORM.from_domain(task)
        self.session.add(orm)
        self.session.commit()
        self.session.refresh(orm)
        return orm.to_domain()

    def get(self, task_id: int) -> Optional[DomainTask]:
        obj = self.session.get(TaskORM, task_id)
        return obj.to_domain() if obj else None
