from pydantic import BaseModel

class AuthUser(BaseModel):
    username:str
    password:str
    
class LoginUser(BaseModel):
    username:str
    password:str