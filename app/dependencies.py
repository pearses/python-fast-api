from fastapi import Depends
from sqlalchemy.orm import Session
from .database import SessionLocal
from .repository.task_repository import taskRepository
from .repository.itask_repository import ItaskRepository
# from .service.task_service_mock import taskServiceMock
from .service.task_service import taskService
from .service.itask_service import ItaskService

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_repository(db: Session = Depends(get_db)) -> ItaskRepository:
    return taskRepository(db)

def get_task_service(repository: ItaskRepository = Depends(get_task_repository)) -> ItaskService:
    return taskService(repository)

# def get_task_service() -> ItaskService:
#     return taskServiceMock()