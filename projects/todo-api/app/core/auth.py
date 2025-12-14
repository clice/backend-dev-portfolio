"""
O que isso faz?
- Lê o token do header Authorization
- Decodifica o JWT
- Busca o usuário no banco
- Injeta o usuário no endpoint
- Isso é Dependency Injection (conceito-chave do FastAPI)
"""

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import decode_token
from app.database.session import SessionLocal
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = decode_token(token)

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    db: Session = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user
