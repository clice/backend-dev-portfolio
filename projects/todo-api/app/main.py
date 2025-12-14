from fastapi import FastAPI
from app.routers.task_router import router as task_router

app = FastAPI(title="To-do API")

app.include_router(task_router)
