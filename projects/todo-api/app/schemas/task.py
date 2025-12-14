"""
Schemas Pydantic relacionados à entidade Task.
Definem entrada e saída da API.
"""

from pydantic import BaseModel
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False


class TaskCreate(TaskBase):
    """
    Dados necessários para criar ou atualizar uma tarefa.
    """
    pass


class TaskResponse(TaskBase):
    """
    Dados retornados pela API.
    """
    id: int

    class Config:
        from_attributes = True
