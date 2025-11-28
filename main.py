from fastapi import FastAPI
from api.v1.routes.translate import translate_router
from api.v1.routes.auth import auth_router
from db.database import engine
from db.models.base import Base
# from core.config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



Base.metadata.create_all(bind=engine)

app.include_router(translate_router , prefix="/api/v1")
app.include_router(auth_router ,prefix="/api/v1")


