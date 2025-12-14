from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserResponse
from app.models.user import User
from app.database.session import SessionLocal
from app.core.security import hash_password

router = APIRouter(prefix="/users", tags=["Users"])
