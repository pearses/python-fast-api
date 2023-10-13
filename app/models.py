# Taken from FastAPI doc: https://fastapi.tiangolo.com/tutorial/body/
from fastapi import FastAPI
from pydantic import BaseModel


class toDo(BaseModel):
    id: int
    item: str