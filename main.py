from fastapi import FastAPI
from db import setup_db
from user.auth import router as auth_router
from appointments import router as appointment_router

setup_db()
app = FastAPI()
app.include_router(auth_router,prefix="/users")
app.include_router(appointment_router,prefix="/appointments")


@app.post("/")
def create_user():
    return {"Hello": "World"}


