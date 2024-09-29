from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db,engine,Base
  # Adjust based on your database session handling
from fastapi.security import OAuth2PasswordBearer
from schemas.Schemas import UserCreate, UserLogin , RegisterResponse, LoginResponse
from sqlalchemy.exc import IntegrityError
from models.Models import User  # Your SQLAlchemy model
from sqlalchemy import text
from auth.utils import hash_password

from seeding import seed_roles

app = FastAPI()

@app.on_event("startup")
def startup_event():
    # Create the database tables
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully!")
    except Exception as e:
        print(f"Error creating database tables: {e}")

        
@app.on_event("startup")
def startup_event():
    db = next(get_db())
    seed_roles(db)


@app.get("/test")
def read_root():
    return {"msg": "Hello Sir! I'm ready to serve you."}

@app.get("/dbtest")
def read_root():
    try:
        with next(get_db()) as db:
            # Wrap the SQL query in text()
            db.execute(text("SELECT 1"))
        return {"msg": "🎉 Database is running smoothly!"}
    except Exception as e:
        return {"msg": "⚠️ Database is not running", "error": str(e)}


@app.post("/register", response_model=RegisterResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Logic for hashing the password, checking existing users, etc.
    
    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password),  # Hash the password
        # password=user.password,  # For testing purposes
        role_id=user.role_id  # Use provided role_id or default logic if needed
    )
    
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"msg": "User registered successfully", "user": new_user}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username or email already registered." )

@app.post("/login" , response_model=LoginResponse)
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    # Logic for hashing the password, checking existing users, etc.
    try:
        db_user = db.query(User).filter(User.username == user.username).first()
        if user:
            if user.password == db_user.password:
                return {"msg": "User logged in successfully", "user": db_user}
            return {"msg": "Invalid password", "user": db_user}
        else:
            raise HTTPException(status_code=400, detail="User not found.")
    except Exception as e:
        raise HTTPException(status_code=400, detail="An error occurred while logging in.")