"""
Configuração da conexão com o banco de dados.
Agora usando PostgreSQL + variáveis de ambiente.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Carrega variáveis do .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o engine do PostgreSQL
engine = create_engine(DATABASE_URL)

# Cria sessões de banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os modelos ORM
Base = declarative_base()
