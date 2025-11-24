from fastapi import FastAPI
from api.v1.routes.translate import translate_router
from db.database import engine
from db.models.base import Base


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(translate_router , prefix="/api/v1")
    

