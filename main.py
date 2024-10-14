from fastapi import FastAPI
from db import setup_db
from user.auth import router

setup_db()
app = FastAPI()
app.include_router(router,prefix="/user")


@app.post("/")
def create_user():
    return {"Hello": "World"}


