"""
O que está acontecendo aqui?
- Criamos a aplicação FastAPI
- Registramos os routers (rotas separadas por domínio)
- O Swagger aparece automaticamente em /docs
"""

from fastapi import FastAPI
from app.routers import auth, users, tasks

app = FastAPI(title="To-do API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)
