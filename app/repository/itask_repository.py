from abc import ABC, abstractmethod
from typing import List, Optional
from ..models.task import task

class ItaskRepository(ABC):
    
    @abstractmethod
    def create(self, task: task) -> task:
        pass
    
    @abstractmethod
    def get(self, task_id: int) -> task:
        pass
    
    @abstractmethod
    def get_all(self) -> List[task]:
        pass
    
    @abstractmethod
    def update(self, task_id: int, updated_data: dict) -> task:
        pass