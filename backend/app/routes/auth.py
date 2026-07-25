from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

from passlib.context import CryptContext

from jose import jwt
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

SECRET_KEY = "your-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



def get_password_hash(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)





router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login(user:UserCreate , db: Session=Depends(get_db)):
    db_user = db.query(User).filter(
    User.username == user.username
    ).first()
    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )
    if not verify_password(user.password,db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(data={'sub': db_user.username})
    return {'access_token': access_token ,'token_type':'bearer'}
    

@router.post('/register')
def register(new_user:UserCreate , db: Session=Depends(get_db)):
    exist= db.query(User).filter(User.username== new_user.username).first()
    if exist:
        raise HTTPException(
            status_code=401,
            detail="User already exists"
        )
    
    hashed_password = get_password_hash(new_user.password)

    db_user = User(
        username=new_user.username,
        password=hashed_password)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
    "message": "User registered successfully"
    }       

    


@router.get('/me')
def me(token: str = Depends(oauth2_scheme),db: Session=Depends(get_db)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    username =payload.get('sub')
    if username is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    exist= db.query(User).filter(User.username==username).first()

    if not exist:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )
    return {
        "username": exist.username
    }

        