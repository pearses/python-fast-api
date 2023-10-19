from typing import List
from fastapi import HTTPException
from ..repository.itask_repository import ItaskRepository
from ..dto.task_dto import taskCreateDTO, taskUpdateDTO, taskDTO
from ..models.task import task as taskDB
from .itask_service import ItaskService


class taskService(ItaskService):
    def __init__(self, repository: ItaskRepository):
        self.repository = repository
    
    def create_task(self, task_create_dto: taskCreateDTO) -> taskDTO:
        db_task = taskDB(**task_create_dto.dict())
        created_task = self.repository.create(db_task)
        return taskDTO.from_orm(created_task)
    
    def get_task(self, task_id: int) -> taskDTO:
        db_task = self.repository.get(task_id)
        return taskDTO.from_orm(db_task)
    
    def get_tasks(self) -> List[taskDTO]:
        db_tasks = self.repository.get_all()
        return [taskDTO.from_orm(db_task) for db_task in db_tasks]

    def update_task(self, task_id: int, task_update_dto: taskUpdateDTO) -> taskDTO:
        updated_data = task_update_dto.dict(exclude_unset=True)
        updated_task = self.repository.update(task_id, updated_data)
        return taskDTO.from_orm(updated_task)
    
    def delete_task(self, task_id: int):
        self.repository.delete(task_id)