from fastapi import  APIRouter , Depends
from services.translate_services import translate_text
from services.auth_service import verify_token
from ..schemas.translate import TranslateRequest

translate_router = APIRouter(prefix="/translate" , tags=["translation"])

@translate_router.post('/')
def translate(request:TranslateRequest, user= Depends(verify_token)):
    
    return {"user": user.username, "translated": translate_text(request.choice, request.text)}