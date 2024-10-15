from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from models import Base
import os

engine=None

def get_engine():
    load_dotenv()
    db_url = os.getenv("DB_URL")
    engine = create_engine(str(db_url),echo=True)
    return engine

def setup_db():
    global engine
    engine = get_engine()
    session = Session(engine,autocommit=False)
    Base.metadata.create_all(engine)


