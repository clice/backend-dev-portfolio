"""
Aqui acontece:
- validação de entrada
- formatação da saída
- integração automática com Swagger
"""

from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    description: str | None = None

class TaskResponse(TaskCreate):
    id: int
    completed: bool

    class Config:
        from_attributes = True
