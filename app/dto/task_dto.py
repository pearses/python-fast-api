from pydantic import BaseModel

class TaskCreateDTO(BaseModel):
    id: int
    item: str

class TaskUpdateDTO(BaseModel):
    id: int
    item: str

class Task(BaseModel):
    id: int
    item: str

    class Config:
        from_attributes = True