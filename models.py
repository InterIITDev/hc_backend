from sqlalchemy import Column,  Integer, String, ForeignKey,DateTime,func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Auth(Base):
    __tablename__="auth"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    username = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    role_id = Column(Integer,nullable=False)

class Patient(Base):
    __tablename__="patients"
    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    auth_id = Column(Integer,ForeignKey("auth.id"))
    name = Column(String,nullable=False)
    dob = Column(String)

class Appointments(Base):
    __tablename__="appointments"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    desc = Column(String)
    patient_id = Column(Integer,ForeignKey('patients.id'))
    timestamp = Column(DateTime(timezone=True),server_default=func.now())
    last_updated_by = Column(Integer,ForeignKey("auth.id"))

class Events(Base):
    __tablename__="events"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    appointment_id = Column(Integer,ForeignKey('appointments.id'))
    desc = Column(String)
    patient_id = Column(Integer,ForeignKey('patients.id'))
    result = Column(String)
    status = Column(String,nullable=False)
    timestamp = Column(DateTime(timezone=True),server_default=func.now())

class Doctor(Base):
    __tablename__="doctors"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    speciality = Column(String)
    qualifications = Column(String,nullable=False)
    shift_timing = Column(String,nullable=False)

class Receptionist(Base):
    __tablename__="receptionists"
    id = Column(Integer,primary_key=True,index=True)
    auth_id = Column(Integer,ForeignKey('auth.id'))
    name = Column(String,nullable=False)
    speciality = Column(String)

class Machinist_Category(Base):
    __tablename__="m_type"
    id = Column(Integer,primary_key=True,index=True)
    category = Column(String,unique=True)

class Machinist(Base):
    __tablename__="machinists"
    id = Column(Integer,primary_key=True,index=True)
    auth_id = Column(Integer,ForeignKey("auth.id"))
    category = Column(String,ForeignKey('m_type.category'))
    name = Column(String,nullable=False)


