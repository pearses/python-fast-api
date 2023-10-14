from fastapi import FastAPI
from .models import ToDo  # Correct the import statement

app = FastAPI()

todolist = []  # Rename to `todolist`

# Post
@app.post("/todolist")  # Use @app.post to create a to-do
async def post_todo(todo: ToDo):  # Use the correct variable name 'todo'
    todolist.append(todo)  # Correct the variable name 'todolist'
    return {"message": "Todo has been added!"}

# Get All
@app.get("/todolist")
async def get_all_todos():
    return {"todolist": todolist}

# Get Single ID
@app.get("/todolist/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todolist:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message":"todo notfound !"}

# Put
@app.put("/todolist/{todo_id}")
async def update_todo(todo_id: int, todo_obj: ToDo):
    for todo in todolist:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            todolist.append(todo)
            return {"message":"todo has been updated !"}
    return {"message":"No todos found !"}

# Delete
@app.delete("/todolist/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todolist:
        if todo.id == todo_id:
            todolist.remove(todo)
            return {"message":"todo has been deleted !"}
    return {"message":"todo not found !"}  
