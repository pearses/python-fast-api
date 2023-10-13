# Taken from FastAPI doc: https://fastapi.tiangolo.com/tutorial/body/
from pydantic import BaseModel


class ToDo(BaseModel):
    id: int
    item: str