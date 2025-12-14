"""
Explicação
- engine → conexão com o banco
- SessionLocal → cria sessões para queries
- Usamos PostgreSQL via Docker (db é o nome do container)
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@db:5432/todo"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
