from sqlalchemy.orm import Session

from . import models, shemas


def create_mashine(db: Session, mashine: shemas.MashineCreate):
    db_mashine = models.Machine(
        name=mashine.name,
        module=mashine.module,
        ip=mashine.ip,
        port=mashine.port,
        type_mashine_id=mashine.type_mashine_id,
        location=mashine.location,
        note=mashine.note,
        status_id=mashine.status_id,
        status_connect=False
    )
    db.add(db_mashine)
    db.commit()
    db.refresh(db_mashine)
    return db_mashine


def change_mashine(id: int, db: Session, mashine: shemas.MashineCreate):
    mashine_db = db.query(models.Machine).filter(models.Machine.id == id).first()
    mashine_db.name = mashine.name
    mashine_db.module = mashine.module
    mashine_db.ip = mashine.ip
    mashine_db.port = mashine.port
    mashine_db.type_mashine_id = mashine.type_mashine_id
    mashine_db.location = mashine.location
    mashine_db.note = mashine.note
    mashine_db.status_id = mashine.status_id
    mashine_db.status_connect = False
    db.commit()
    db.refresh(mashine_db)
    return mashine_db

def delete_mashine(id: int, db: Session):
    mashine_db = db.query(models.Machine).filter(models.Machine.id == id).first()
    if mashine_db:
        db.delete(mashine_db)
        db.commit()
        return {
            'status': True,
            'text': 'Запись удалена'
        }
    else:
        return {
            'status': False,
            'text': 'Запись не найдена'
        }


def get_all_mashine(db: Session):
    all_mash = db.query(models.Machine).order_by(models.Machine.id.asc()).all()
    for mash in all_mash:
        mash.status
        mash.type_mash
    return all_mash

def get_all_mashine_status(db: Session):
    all_mash = db.query(models.Machine).order_by(models.Machine.id.asc()).all()
    status_list = []
    for mash in all_mash:
        mash_status = {
            "id": mash.id,
        }
        if mash.status_connect:
            mash_status["status"] = {
                "text": "Подключено",
                "color": "#6FCF97"
            }
        else:
            mash_status["status"] = {
                "text": "Не найдено",
                "color": "#EB5757"
            }
        status_list.append(mash_status)
    return status_list

def get_mashine_by_id(db: Session, id: int):
    return db.query(models.Machine).filter(models.Machine.id == id).first()


def get_all_type_mash(db: Session):
    return db.query(models.TypeMashine).all()

def get_type_by_id(db: Session, id: int):
    return db.query(models.TypeMashine).filter(models.TypeMashine.id == id).first()

def get_all_status_mash(db: Session):
    return db.query(models.StatusMashine).all()

def get_status_by_id(db: Session, id: int):
    return db.query(models.StatusMashine).filter(models.StatusMashine.id == id).first()

def get_shifts(db: Session):
    return db.query(models.ShiftWorkshop).order_by(models.ShiftWorkshop.id.asc()).all()

def add_shifts(db: Session, shifts: list[shemas.ShiftShow]):
    old_shifts = get_shifts(db=db)
    for shift in old_shifts:
        db.delete(shift)
        db.commit()
    new_list_shift = []
    for index, shift in enumerate(shifts):
        shift_db = models.ShiftWorkshop(
            id=index+1,
            name=index+1,
            start=shift.start,
            end=shift.end
        )
        db.add(shift_db)
        db.commit()
        db.refresh(shift_db)
        new_list_shift.append(shift_db)
    return new_list_shift