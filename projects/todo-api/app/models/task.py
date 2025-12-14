"""
Modelo da tabela de tarefas.
Cada instância representa uma linha no banco.
"""

from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Task(Base):
    """
    Tabela 'tasks' do banco de dados.
    """
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    done = Column(Boolean, default=False)
