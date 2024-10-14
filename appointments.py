from fastapi import APIRouter
from sqlalchemy.orm import Session
from db import get_engine
from models import Appointments
from pydantic import BaseModel

class NewAppointment(BaseModel):
    username: str
    desc: str

router = APIRouter()

@router.post("/")
def book_appointment(info:NewAppointment):
    engine = get_engine()
    with Session(engine) as session:
        appointment = Appointments(patient_id=info.username,desc=info.desc,last_updated_by=info.username)
        session.add(appointment)
        session.commit()



