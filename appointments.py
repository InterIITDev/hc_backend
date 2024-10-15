from fastapi import APIRouter,status
from sqlalchemy.orm import Session
from sqlalchemy import select
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

@router.get("/{id}")
def get_appointment(id:int):
    stmt = select(Appointments).where(Appointments.id==id)
    engine = get_engine()
    with Session(engine) as session:
        user = session.scalars(stmt).one_or_none()
        return user


class UpdateAppointment(BaseModel):
    doctor_id: str | None = None
    desc: str | None = None

@router.put("/{id}")
def update_appointment(id:int,updates:UpdateAppointment):
    # Add Check
    stmt = select(Appointments).where(Appointments.id==id)
    engine = get_engine()
    with Session(engine) as session:
        user = session.scalars(stmt).one_or_none()
        if user is not None:
            if updates.doctor_id is not None:
                setattr(user,'doctor_id',updates.doctor_id)
            if updates.desc is not None:
                setattr(user,'desc',updates.desc)
        session.commit()
        return status.HTTP_200_OK



