from pydantic import BaseModel
class TranslateRequest(BaseModel):
    choice: str
    text: str