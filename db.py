from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from models import Base
import os

load_dotenv()
db_url = os.getenv("DB_URL")
engine = create_engine(str(db_url),echo=True)
session = Session(engine,autocommit=False)
Base.metadata.create_all(engine)


