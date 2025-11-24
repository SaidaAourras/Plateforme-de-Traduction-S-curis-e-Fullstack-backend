from fastapi import APIRouter
from ..schemas.user import AuthUser
from fastapi import Depends
from sqlalchemy.orm import Session
from api.v1.dependencies import get_db
from services.auth_service import create_user , authenticate_user

auth_router = APIRouter(prefix='/auth',tags=["authentication"])

@auth_router.post('/register')
def register(user:AuthUser , db:Session = (Depends(get_db))):
     return create_user(user,db)

@auth_router.post('/login')
def login(user:AuthUser , db:Session = (Depends(get_db))):
     return authenticate_user(user,db)
