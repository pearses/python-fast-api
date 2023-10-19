from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ..models.task import task
from .itask_repository import ItaskRepository

class taskRepository(ItaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, task: task) -> task:
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def find(self, task_id: int) -> Optional[task]:
        return self.db.query(task).filter(task.id == task_id).first()
    
    def get(self, task_id: int) -> task:
        task_db = self.find(task_id)
        if task_db:
            return task_db    
        raise HTTPException(status_code=404, detail="task not found")

    
    def get_all(self) -> List[task]:
        return self.db.query(task).all()
    
    def update(self, task_id: int, updated_data: dict) -> task:
        db_task = self.get(task_id)

        # Update the SQLAlchemy model instance with data from the Pydantic model
        for key, value in updated_data.tasks():
            setattr(db_task, key, value)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task
    
    def delete(self, task_id: int):
        db_task = self.get(task_id)
        if db_task:
            self.db.delete(db_task)
            self.db.commit()