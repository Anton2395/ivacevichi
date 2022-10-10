from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Users import models as models_user
from Users.views import app as app_user
from Machine import models as models_mashine
from Machine.views import app as app_mashine
from database import engine

models_user.Base.metadata.create_all(bind=engine)
models_mashine.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(app_user)
app.include_router(app_mashine)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)