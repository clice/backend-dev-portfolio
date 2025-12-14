"""
Explicação
- EmailStr → valida formato de e-mail
- min_length=6 → regra mínima de segurança
- UserResponse não tem senha
- from_attributes → converte SQLAlchemy → Pydantic
"""

from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
