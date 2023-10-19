from typing import List, Optional
from ..dto.task_dto import taskCreateDTO, taskUpdateDTO, taskDTO
from .itask_service import ItaskService

class taskServiceMock(ItaskService):
    def __init__(self):
        # Creating some hardcoded tasks
        self.tasks = [
            taskDTO(id=1, name="task One", description="This is task one."),
            taskDTO(id=2, name="task Two", description="This is task two."),
        ]
    
    def create_task(self, task_create: taskCreateDTO) -> taskDTO:
        # Creating a new task with id=3
        new_task = taskDTO(id=3, name=task_create.name, description=task_create.description)
        return new_task
    
    def get_task(self, task_id: int) -> taskDTO:
        # Returning a hardcoded task if it exists in the list, else None
        task = next((task for task in self.tasks if task.id == task_id), None)
        return task
    
    def get_tasks(self) -> List[taskDTO]:
        # Returning the list of hardcoded tasks
        return self.tasks
    
    def update_task(self, task_id: int, task_update: taskUpdateDTO) -> taskDTO:
        # Updating the task if it exists and returning it, else returning a default task
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            task.name = task_update.name or task.name
            task.description = task_update.description or task.description
            return task
        else:
            return taskDTO(id=0, name="Default", description="Default task")
    
    def delete_task(self, task_id: int):
        # Deleting the task if it exists in the hardcoded list
        self.tasks = [task for task in self.tasks if task.id != task_id]