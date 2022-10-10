import hashlib

from sqlalchemy.orm import Session

from . import models, shemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: shemas.UserCreate):
    hash_password = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = models.User(
        username=user.username,
        hashed_password=hash_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(password:str, user: models.User):
    return hashlib.sha256(password.encode()).hexdigest().lower() == user.hashed_password.lower()