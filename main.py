from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import houses, users
from auth import authentication
from db import models
from db.database import engine

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(houses.router)
app.include_router(users.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(engine)