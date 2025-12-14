from fastapi import FastAPI
from app.database import engine
from app.models.task import Task
from app.routers.task_router import router as task_router

# Cria tabelas
Task.metadata.create_all(bind=engine)

app = FastAPI(title="To-do API")

# Registra as rotas
app.include_router(task_router)
