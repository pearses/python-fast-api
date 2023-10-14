from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models import ToDo  # models.py
# -- IMPORT SERVICE --
# from ..dependencies import get_item_service
# -- IMPORT INTERFACE SERVICE --
# from ..service.iitem_service import IItemService 
# -- IMPORT DTOS --
# from ..dto.item_dto import ItemCreateDTO, ItemUpdateDTO, ItemDTO -- IMPORT DTOS

router = APIRouter(prefix="/api/todolist")

todolist = []  # Rename to `todolist`

# Post
@router.post("/todolist")  # Use @app.post to create a to-do
async def post_todo(todo: ToDo):  # Use the correct variable name 'todo'
    todolist.append(todo)  # Correct the variable name 'todolist'
    return {"message": "Todo has been added!"}

# Get All
@router.get("/todolist")
async def get_all_todos():
    return {"todolist": todolist}

# Get Single ID
@router.get("/todolist/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todolist:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message":"todo notfound !"}

# Put
@router.put("/todolist/{todo_id}")
async def update_todo(todo_id: int, todo_obj: ToDo):
    for todo in todolist:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            todolist.append(todo)
            return {"message":"todo has been updated !"}
    return {"message":"No todos found !"}

# Delete
@router.delete("/todolist/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todolist:
        if todo.id == todo_id:
            todolist.remove(todo)
            return {"message":"todo has been deleted !"}
    return {"message":"todo not found !"}  
