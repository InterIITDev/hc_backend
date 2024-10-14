from fastapi import APIRouter,status
from sqlalchemy.orm import Session
from sqlalchemy import select
from pydantic import BaseModel
from db import get_engine
from models import Auth
router = APIRouter()

class NewUser(BaseModel):
    username: str
    name: str | None
    password: str
    role_id: int

class UserLogin(BaseModel):
    username: str
    password: str

class ChPasswd(BaseModel):
    username: str
    password: str
    new_passwd: str

@router.post("/register")
def create_user(new_user:NewUser):
    user = Auth(username=new_user.username,name=new_user.name,password=new_user.password,role_id=new_user.role_id)
    engine = get_engine()
    with Session(engine) as session:
        session.add(user)
        session.commit()
    return status.HTTP_201_CREATED

@router.post("/login")
def login_user(old_user:NewUser):
    stmt = select(Auth).where(Auth.username==old_user.username)
    engine = get_engine()
    with Session(engine) as session:
        user = session.scalars(stmt).one_or_none()
        if user is not None:
            if str(user.password) == old_user.password:
                return status.HTTP_200_OK
            else:
                return status.HTTP_401_UNAUTHORIZED
        else:
            return status.HTTP_404_NOT_FOUND
