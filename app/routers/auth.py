from fastapi import *
from sqlalchemy import *
from sqlalchemy.util import deprecated
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas import CreateUser
from app.backend.db_depends import get_db
from typing import Annotated
from passlib.context import CryptContext

from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()

router = APIRouter(prefix="/auth", tags=['auth'])
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(insert(User).values(
        first_name = create_user.first_name,
        last_name=create_user.last_name,
        username=create_user.username,
        email=create_user.email,
        hashed_password=bcrypt_context.hash(create_user.password),
    ))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }

async def get_current_username(db: Annotated[Session, Depends(get_db)], credentials: HTTPBasicCredentials = Depends(security)):
    user = db.scalar(select(User).where(User.username == credentials.username))
    if not user or not bcrypt_context.verify(credentials.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


@router.get('/users/me')
async def read_current_user(user: str = Depends(get_current_username)):
    return {'User': user}