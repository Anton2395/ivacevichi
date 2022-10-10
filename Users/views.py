from datetime import timedelta
import time

from fastapi import APIRouter, Depends, Request, Response
# from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException


from settings import SECRET_KEY, PASSWORD_SALT
from database import SessionLocal, get_db
from . import models, service, shemas
from .auth_handler import signJWT, getUser
from .auth_bearer import JWTBearer

app = APIRouter()


def get_user(login: str):
    db = SessionLocal()
    user = db.query(models.User).filter(models.User.username == login).first()
    db.close()
    return user

@app.get("/role", tags=["User"])
def check_role(request: Request, db: Session = Depends(get_db)):
    print(dir(request))
    print(request.headers)
    if request.cookies.get('access_token'):
        user_name = getUser(request.cookies['access_token'])
        user_db = db.query(models.User).filter(models.User.username == user_name).first()
        role = user_db.role
    else:
        role = "guest"
    return role

@app.post('/login', tags=["User"])
def login(user: shemas.UserLogin, response: Response, db: Session = Depends(get_db)):
    login = user.username
    password = user.password

    user = get_user(login)
    if not user:
        raise InvalidCredentialsException  
    elif not service.verify_password(password=password+PASSWORD_SALT, user=user):
        raise InvalidCredentialsException
    user.status = True
    db.commit()
    content = signJWT(user.username)
    content['role'] = user.role
    response.set_cookie(key='access_token', value=content['access_token']) 
    time.sleep(2) 
    return content

@app.post('/user', response_model=shemas.User, tags=["User"])
def create_user(user: shemas.UserCreate, db: Session = Depends(get_db)):
    user.password += PASSWORD_SALT
    return service.create_user(db=db, user=user)
