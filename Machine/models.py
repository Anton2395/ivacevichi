from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Time
from sqlalchemy.orm import relationship

from database import Base


class Machine(Base):
    __tablename__ = "mashine"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    module = Column(String, default="")
    ip = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    type_mashine_id = Column(Integer, ForeignKey('type_mashine.id'), nullable=False)
    location = Column(String, default="")
    note = Column(String, default="")
    status_id = Column(Integer, ForeignKey('status_mashine.id'), nullable=False)
    status_connect = Column(Boolean, nullable=True, default="")
    status = relationship('StatusMashine', back_populates="mashine")
    type_mash = relationship('TypeMashine', back_populates="mashine")
    


class StatusMashine(Base):
    __tablename__ = "status_mashine"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False, default="Неизвестно")
    color = Column(String, nullable=False, default="#000")
    mashine = relationship('Machine', cascade="all, delete", back_populates="status")

class TypeMashine(Base):
    __tablename__ = "type_mashine"
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False, default="Неизвестно")
    value = Column(Integer, nullable=False, default=0)
    mashine = relationship('Machine', cascade="all, delete", back_populates="type_mash")

class ShiftWorkshop(Base):
    __tablename__ = "shift_mashine"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True, default="Нет названия")
    start = Column(Time, nullable=False)
    end = Column(Time, nullable=False)
    