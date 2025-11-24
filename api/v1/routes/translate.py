from fastapi import  APIRouter
from services.translate_services import translate_text

translate_router = APIRouter(prefix="/translate" , tags=["translation"])

@translate_router.post('/{choice}')
def translate(choice: str , text: str):
    return translate_text(choice , text)