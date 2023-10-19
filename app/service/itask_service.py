from typing import List
from ..dto.task_dto import taskCreateDTO, taskUpdateDTO, taskDTO

class ItaskService:
    def create_task(self, task_create_dto: taskCreateDTO) -> taskDTO:
        raise NotImplementedError

    def get_task(self, task_id: int) -> taskDTO:
        raise NotImplementedError

    def get_tasks(self) -> List[taskDTO]:
        raise NotImplementedError

    def update_task(self, task_id: int, task_update_dto: taskUpdateDTO) -> taskDTO:
        raise NotImplementedError

    def delete_task(self, task_id: int):
        raise NotImplementedError