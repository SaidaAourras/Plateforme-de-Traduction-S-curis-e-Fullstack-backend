from db.models.user import User
from utils.hashing import get_hash_password , verify_password
from fastapi import HTTPException ,Depends , status
from jose import jwt , JWTError
from dotenv import load_dotenv
import os
from fastapi.security import OAuth2PasswordBearer
from api.v1.dependencies import get_db
# from fastapi.security import APIKeyHeader

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")
# key_api_header = APIKeyHeader(name='Authorization')

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_user(user , db):
    new_user = User(
        username=user.username,
        password_hash = get_hash_password(user.password)
     )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user 

def authenticate_user(user, db):
    # D'abord, récupérer l'utilisateur par username
    logged_user = db.query(User).filter(User.username == user.username).first()
    
    if not logged_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not verify_password(user.password, logged_user.password_hash):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    # Convertir la date dans un format compatible JSON
    data = {
        'username': logged_user.username,
        'created_at': logged_user.created_at.isoformat()
    }
    
    access_token = create_token(data)
    
    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }



def create_token(data:dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode ,SECRET_KEY, algorithm=ALGORITHM )
    return encoded_jwt



def verify_token(db = Depends(get_db) , token:str = Depends(oauth2_scheme)):
    try:

        payload = jwt.decode(token , SECRET_KEY , algorithms=ALGORITHM)
        user = db.query(User).filter(User.username == payload['username']).first()
        
        return user
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
                detail='token invalide',
                headers={"WWW-Authenticate": "Bearer"}
        )

        


    