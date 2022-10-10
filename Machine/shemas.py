import datetime
from typing import Optional
from pydantic import BaseModel


class TypeMashineCreate(BaseModel):
    text: str
    value: int
    
    class Config:
        orm_mode = True
    

class TypeMashine(TypeMashineCreate):
    id: int
    
    class Config:
        orm_mode = True
        

class StatusMashineCreate(BaseModel):
    text: str
    color: str
    
    class Config:
        orm_mode = True


class StatusMashine(StatusMashineCreate):
    id: int
    
    class Config:
        orm_mode = True

class MashineCreate(BaseModel):
    name: str
    module: str
    ip: str
    port: int
    type_mashine_id: int
    location: str
    note: str
    status_id: int
    
    class Config:
        orm_mode = True

class MashineShowe(BaseModel):
    name: str
    module: str
    ip: str
    port: int
    type_mash: TypeMashine
    location: str
    note: str
    status: StatusMashineCreate
    
    class Config:
        orm_mode = True

class Mashine(MashineShowe):
    id: int




class DurationTimeGood(BaseModel):
    start: datetime.datetime
    end: datetime.datetime
    duration_seconds: float

class ParamMashine(BaseModel):
    name_mashine: str
    date: str
    shift: str
    duration_work: float
    duration_power: float
    duration_bad: float
    count_processed_parts: int = None
    count_facings: int = None
    conveyor_speed: int = None
    count_processed_boards: int = None


class ParamMashineNow(BaseModel):
    name_mashine: str
    duration_work: float
    duration_power: float
    duration_bad: float
    status_power: bool
    status_connect: StatusMashineCreate

class ShiftShow(BaseModel):
    id: int
    start: datetime.time
    end: datetime.time
    
    class Config:
        orm_mode = True