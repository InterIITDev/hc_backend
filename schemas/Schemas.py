from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: str
    password: str  # Consider using hashed passwords in a real application
    is_active: bool = True
    role_id: int = None    # Default role_id for new users

class UserCreate(UserBase):
    pass  # Additional fields for creation if needed

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    role_id: int = None
    class Config:
        orm_mode = True  # Enables compatibility with SQLAlchemy models
    
class RegisterResponse(BaseModel):
    msg: str
    user: UserResponse  # Nest the UserResponse model inside

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    msg: str
    user: UserResponse

    class Config:
        orm_mode = True

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleResponse(RoleBase):
    id: int

    class Config:
        orm_mode = True

class OtpBase(BaseModel):
    otp: str
    user_id: int
    is_active: bool = True

class OtpResponse(OtpBase):
    id: int

    class Config:
        orm_mode = True
