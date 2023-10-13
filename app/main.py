from fastapi import FastAPI
from models import toDo

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []


# Get All

@app.get("/todos")
async def get_all_todos():
    return {"todos": toDo}


# Get Single ID
@app.get("/todos/{todo_id}")
async def read_item(todo_id):
    return {"id": todo_id}

# Post 
@app.get("/todos")
async def post_todo(todo: toDo):
    todo.append(todo)
    return {"message": "Todo has been added !"}

# Put



# Delete