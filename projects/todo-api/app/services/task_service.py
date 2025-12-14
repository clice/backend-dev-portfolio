"""
Camada de regras de negócio da aplicação.
"""

from sqlalchemy.orm import Session
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate
from app.models.task import Task


class TaskService:
    """
    Regras de negócio relacionadas às tarefas.
    """

    def __init__(self):
        self.repository = TaskRepository()

    def list_tasks(self, db: Session):
        return self.repository.get_all(db)

    def get_task(self, db: Session, task_id: int):
        return self.repository.get_by_id(db, task_id)

    def create_task(self, db: Session, task_data: TaskCreate):
        task = Task(**task_data.model_dump())
        return self.repository.create(db, task)

    def update_task(self, db: Session, task_id: int, task_data: TaskCreate):
        task = self.repository.get_by_id(db, task_id)
        if not task:
            return None

        for field, value in task_data.model_dump().items():
            setattr(task, field, value)

        db.commit()
        db.refresh(task)
        return task

    def delete_task(self, db: Session, task_id: int):
        task = self.repository.get_by_id(db, task_id)
        if not task:
            return None

        self.repository.delete(db, task)
        return True
