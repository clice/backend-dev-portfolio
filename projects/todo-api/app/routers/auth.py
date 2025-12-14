from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.core.security import verify_password, create_token
from app.database.session import SessionLocal
from app.models.user import User

router = APIRouter()

@router.post("/login")
def login(email: str, password: str):
    db: Session = SessionLocal()
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(user.id)
    return {"access_token": token, "token_type": "bearer"}
