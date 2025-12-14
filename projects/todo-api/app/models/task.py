"""
Cada tarefa pertence a um usuário
"""

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
