import time
from fastapi import APIRouter, Depends, Response
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from . import shemas, service, service_param_mashine
from database import get_db
from Users.auth_bearer import JWTBearer
from database import engine

app = APIRouter(prefix='/mashine')


@app.get('', response_model=list[shemas.Mashine], dependencies=[Depends(JWTBearer())], tags=["Mashine"])
def get_all_mashine(db: Session = Depends(get_db)):
    return service.get_all_mashine(db=db)


@app.get('/status', dependencies=[Depends(JWTBearer())], tags=["Mashine"])
def get_all_mashine_status(db: Session = Depends(get_db)):
    return service.get_all_mashine_status(db=db)


@app.get('/{id}', response_model=shemas.Mashine, dependencies=[Depends(JWTBearer())], tags=["Mashine"])
def get_mahine_by_id(id: int, db: Session = Depends(get_db)):
    return service.get_mashine_by_id(db=db, id=id)


@app.post('', response_model=shemas.Mashine, dependencies=[Depends(JWTBearer())], tags=["Mashine"])
def create_mashine(mashine: shemas.MashineCreate, db: Session = Depends(get_db)):
    return service.create_mashine(db=db, mashine=mashine)


@app.put('/{id}', response_model=shemas.Mashine, dependencies=[Depends(JWTBearer())], tags=["Mashine"])
def change_mashine(id: int, mashine: shemas.MashineCreate, db: Session = Depends(get_db)):
    return service.change_mashine(id=id, mashine=mashine, db=db)


@app.delete('/{id}', dependencies=[Depends(JWTBearer())], tags=["Mashine"])
def delete_mashine(id: int, db: Session = Depends(get_db)):
    return service.delete_mashine(id=id, db=db)


@app.get('/type/', response_model=list[shemas.TypeMashine], dependencies=[Depends(JWTBearer())], tags=["Type"])
def get_all_type(db: Session = Depends(get_db)):
    return service.get_all_type_mash(db=db)


@app.get('/type/{id}', response_model=shemas.TypeMashine, dependencies=[Depends(JWTBearer())], tags=["Type"])
def get_type(id: int, db: Session = Depends(get_db)):
    return service.get_type_by_id(id=id, db=db)


@app.get('/status/', response_model=list[shemas.StatusMashine], dependencies=[Depends(JWTBearer())], tags=["Status"])
def get_all_status(db: Session = Depends(get_db)):
    return service.get_all_status(db=db)


@app.get('/status/{id}', response_model=shemas.StatusMashine, dependencies=[Depends(JWTBearer())], tags=["Status"])
def get_status(id: int, db: Session = Depends(get_db)):
    return service.get_status_by_id(db=db, id=id)


@app.get('/shift/', response_model=list[shemas.ShiftShow], tags=["Shift"])
def get_all_shift(db: Session = Depends(get_db)):
    return service.get_shifts(db=db)


@app.post('/shift/', response_model=list[shemas.ShiftShow], dependencies=[Depends(JWTBearer())], tags=["Shift"])
def add_new_shift(shifts: list[shemas.ShiftShow], db: Session = Depends(get_db)):
    return service.add_shifts(db=db, shifts=shifts)


# @app.get('/data/{id}', response_model=shemas.ParamMashine, dependencies=[Depends(JWTBearer())], tags=["Param"])
# def get_param_mashine(id: int, db: Session = Depends(get_db)):
#     return service.get_param_mashine(id=id, db=db)

@app.get('/data/time/{start}/{end}',
         response_model=list[shemas.ParamMashine],
         dependencies=[Depends(JWTBearer())],
         tags=["Param"])
def get_param_machine_day(start: int, end: int, db: Session = Depends(get_db)):
    return service_param_mashine.get_param_machine_day(db=db, start_date=start, end_date=end)


@app.get('/param/now', response_model=list[shemas.ParamMashineNow], tags=["Param"])
def get_param_machine_now(db: Session = Depends(get_db)):
    return service_param_mashine.get_param_machine_now(db=db)
