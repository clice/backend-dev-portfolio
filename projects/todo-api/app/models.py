"""
Aqui definimos as tabelas do banco de dados.
Cada classe representa uma tabela.
"""

from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Task(Base):
    """
    Modelo da tabela 'tasks'.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
