from fastapi import FastAPI
from models import ToDo  # Correct the import statement

app = FastAPI()

todolist = []  # Rename to `todolist`

# Get All
@app.get("/todolist")
async def get_all_todos():
    return {"todolist": todolist}

# Get Single ID
@app.get("/todolist/{todo_id}")
async def read_item(todo_id):
    return {"id": todo_id}

# Post
@app.post("/todolist")  # Use @app.post to create a to-do
async def post_todo(todo: ToDo):  # Use the correct variable name 'todo'
    todolist.append(todo)  # Correct the variable name 'todolist'
    return {"message": "Todo has been added!"}

# Put

# Delete
