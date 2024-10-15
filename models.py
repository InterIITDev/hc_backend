from sqlalchemy import Column,  Integer, String, ForeignKey,DateTime,func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Auth(Base):
    __tablename__="auth"
    username = Column(String,primary_key=True,unique=True,index=True)
    name = Column(String,nullable=False)
    password = Column(String,nullable=False)
    role_id = Column(Integer,nullable=False)

class Patient(Base):
    __tablename__="patients"
    username = Column(String,ForeignKey("auth.username"),primary_key=True)
    name = Column(String,nullable=False)

class Appointments(Base):
    __tablename__="appointments"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    desc = Column(String)
    patient_id = Column(String,ForeignKey('patients.username'),nullable=False)
    doctor_id = Column(String,ForeignKey('doctors.username'),nullable=True)
    timestamp = Column(DateTime(timezone=True),server_default=func.now())
    last_updated_by = Column(String,ForeignKey("auth.username"))

class Events(Base):
    __tablename__="events"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    appointment_id = Column(Integer,ForeignKey('appointments.id'))
    desc = Column(String)
    patient_id = Column(String,ForeignKey('patients.username'))
    result = Column(String,nullable=True)
    status = Column(String,nullable=False)
    timestamp = Column(DateTime(timezone=True),server_default=func.now())

class Doctor(Base):
    __tablename__="doctors"

    username = Column(String,ForeignKey("auth.username"),primary_key=True,unique=True)
    speciality = Column(String)
    qualifications = Column(String,nullable=False)
    shift_timing = Column(String,nullable=True)

class Receptionist(Base):
    __tablename__="receptionists"
    username = Column(String,ForeignKey("auth.username"),primary_key=True,index=True)

class Machinist_Category(Base):
    __tablename__="m_type"
    category = Column(String,unique=True,primary_key=True)

class Machinist(Base):
    __tablename__="machinists"
    username = Column(String,ForeignKey("auth.username"),primary_key=True,index=True)
    category = Column(String,ForeignKey('m_type.category'))


