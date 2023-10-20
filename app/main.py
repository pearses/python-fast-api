from fastapi import FastAPI
from app.controller import task_controller

app = FastAPI()

app.include_router(task_controller.router, tags=["tasks"])