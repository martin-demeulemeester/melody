from fastapi import FastAPI

from .routes.health import router as health_router
from .routes.tracks import router as tracks_router
from .routes.albums import router as albums_router
from .routes.auth import router as auth_router

from .db import Base, engine
from . import models


app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(health_router)
app.include_router(tracks_router)
app.include_router(albums_router)
app.include_router(auth_router)