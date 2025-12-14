from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
import jwt

from .database import SessionLocal
from .models import User
from .auth import SECRET_KEY, ALGORITHM

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
    authorization: str = Header(...),
    db: Session = Depends(get_db)
):
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload["sub"]
    except:
        raise HTTPException(status_code=401)

    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401)

    return user
