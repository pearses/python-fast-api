from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models import task  # models.py
# -- IMPORT SERVICE --
# from ..dependencies import get_item_service
# -- IMPORT INTERFACE SERVICE --
# from ..service.iitem_service import IItemService 
# -- IMPORT DTOS --
# from ..dto.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemDTO -- IMPORT DTOS

router = APIRouter(prefix="/api/tasklist")

tasklist = []  # Rename to `tasklist`

# Post
@router.post("/tasklist")  # Use @app.post to create a to-do
async def post_task(task: task):  # Use the correct variable name 'task'
    tasklist.append(task)  # Correct the variable name 'tasklist'
    return {"message": "task has been added!"}

# Get All
@router.get("/tasklist")
async def get_all_tasks():
    return {"tasklist": tasklist}

# Get Single ID
@router.get("/tasklist/{task_id}")
async def get_task(task_id: int):
    for task in tasklist:
        if task.id == task_id:
            return {"task": task}
    return {"message":"task not found !"}

# Put
@router.put("/tasklist/{task_id}")
async def update_task(task_id: int, task_obj: task):
    for task in tasklist:
        if task.id == task_id:
            task.id = task_id
            task.item = task_obj.item
            tasklist.append(task)
            return {"message":"task has been updated !"}
    return {"message":"No tasks found !"}

# Delete
@router.delete("/tasklist/{task_id}")
async def delete_task(task_id: int):
    for task in tasklist:
        if task.id == task_id:
            tasklist.remove(task)
            return {"message":"task has been deleted !"}
    return {"message":"task not found !"}  
