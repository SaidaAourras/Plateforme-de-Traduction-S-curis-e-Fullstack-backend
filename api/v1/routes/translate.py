from fastapi import  APIRouter , Depends
from services.translate_services import translate_text
from services.auth_service import verify_token

translate_router = APIRouter(prefix="/translate" , tags=["translation"])

@translate_router.post('/{choice}')
def translate(choice: str , text: str, user= Depends(verify_token)):
    
    return {"user": user.username, "translated": translate_text(choice, text)}