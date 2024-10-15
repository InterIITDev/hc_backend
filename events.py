from fastapi import APIRouter,UploadFile
from sqlalchemy.orm import Session
from sqlalchemy import select
from db import get_engine
from models import Events
from pydantic import BaseModel
import random
import string
import pickle as pk

class NewEvent(BaseModel):
    appointment_id: int
    desc: str | None = None
    patient_id: str
    status: str

router = APIRouter()

@router.post("/")
def create_event(info:NewEvent):
    engine = get_engine()
    with Session(engine) as session:
        event = Events(patient_id=info.patient_id,desc=info.desc,status=info.status,appointment_id=info.appointment_id)
        session.add(event)
        session.commit()

@router.put("/{id}/upload")
def add_file(id:int,file:UploadFile):
    if file.filename is None:
        return
    fname = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + str(file.filename)
    with open(f"uploads/{fname}",'wb') as f:
        pk.dump(file.file,f)
    stmt = select(Events).where(Events.id==id)
    engine = get_engine()
    with Session(engine) as session:
        event = session.scalars(stmt).one()
        setattr(event,'result',fname)
        session.commit()


@router.get("/{id}")
def get_appointment(id:int):
    stmt = select(Events).where(Events.id==id)
    engine = get_engine()
    with Session(engine) as session:
        event = session.scalars(stmt).one_or_none()
        return event


