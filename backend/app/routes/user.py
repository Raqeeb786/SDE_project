from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = User(
        username=user.username,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@router.get('/',response_model=list[UserResponse])
def get_users(db:Session= Depends(get_db)):
    users= db.query(User).all()
    return users

@router.delete('/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return {'message': 'User deleted successfully' if user else 'User not found'}

@router.put('/{user_id}')
def update_user(user_id:int,username:str,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        db.commit()
        db.refresh(user)
        return user
    else:
        return {'message': 'User not found'}



@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = (
        db.query(User)
        .filter(
            User.username == user.username,
            User.password == user.password,
        )
        .first()
    )

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return db_user