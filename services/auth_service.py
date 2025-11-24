from db.models.user import User
from utils.hashing import get_hash_password , verify_password
from fastapi import HTTPException
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

def create_user(user , db):
    new_user = User(
        username=user.username,
        password_hash = get_hash_password(user.password)
     )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user 

def authenticate_user(user , db):
    logged_user = db.query(User).filter(User.username == user.username and verify_password(user.password , User.password)).first()
    if not logged_user:
        raise HTTPException(status_code=400, detail="Inactive user")
    return {'success':'you logged in'}
