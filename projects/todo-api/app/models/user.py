"""
Importante
- Isso não é validação
- É estrutura do banco
- Quem valida dados é o Pydantic
"""

from sqlalchemy import Column, Integer, String
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
