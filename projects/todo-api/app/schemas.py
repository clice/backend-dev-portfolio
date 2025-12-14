"""
Schemas definem como os dados entram e saem da API.
Eles NÃO falam com o banco diretamente.
"""

from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskCreate(TaskBase):
    """
    Usado quando o cliente CRIA uma tarefa.
    """
    pass


class TaskResponse(TaskBase):
    """
    Usado quando a API DEVOLVE uma tarefa.
    """
    id: int

    class Config:
        from_attributes = True
