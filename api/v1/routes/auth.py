from fastapi import APIRouter
from ..schemas.user import AuthUser
from fastapi import Depends
from sqlalchemy.orm import Session
from api.v1.dependencies import get_db
from services.auth_service import create_user , authenticate_user
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(prefix='/auth',tags=["authentication"])

@auth_router.post('/register')
def register(user:AuthUser , db:Session = (Depends(get_db))):
     return create_user(user,db)

@auth_router.post('/login')
def login(form:OAuth2PasswordRequestForm = Depends(), db:Session = (Depends(get_db))):
     data = AuthUser(username=form.username, password=form.password)
     return authenticate_user(data,db)
