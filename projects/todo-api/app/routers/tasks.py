from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.task import TaskCreate, TaskResponse
from app.database.session import SessionLocal
from app.models.task import Task
from app.models.user import User
from app.core.auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate):
    db: Session = SessionLocal()

    # Verifica se o email já existe
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Cria usuário com senha hasheada
    new_user = User(
        email=user.email,
        password_hash=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/", response_model=list[TaskResponse])
def list_tasks():
    db: Session = SessionLocal()
    return db.query(Task).filter(Task.user_id == 1).all()

@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
):
    db: Session = SessionLocal()

    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/", response_model=list[TaskResponse])
def list_tasks(current_user: User = Depends(get_current_user)):
    db: Session = SessionLocal()

    return (
        db.query(Task)
        .filter(Task.user_id == current_user.id)
        .all()
    )

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
):
    db: Session = SessionLocal()

    db_task = (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == current_user.id)
        .first()
    )

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task.title
    db_task.description = task.description

    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
):
    db: Session = SessionLocal()

    task = (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == current_user.id)
        .first()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"detail": "Task deleted"}
