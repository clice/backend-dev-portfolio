"""
Este arquivo cuida EXCLUSIVAMENTE da conexão com o banco de dados.
Aqui usamos SQLite para facilitar o início.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL do banco (arquivo local SQLite)
DATABASE_URL = "sqlite:///./todo.db"

# Cria o motor de conexão
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria sessões para conversar com o banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Classe base para os modelos
Base = declarative_base()
