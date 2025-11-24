from fastapi import FastAPI
from hagging_face__en_fr import english_to_frensh
from hagging_face_fr_en import frensh_to_english

app = FastAPI()


@app.post('/translate/{choice}')
def translate(choice:str , text:str):
    user_text = text
    if (choice == 'en-fr'):
        return english_to_frensh(user_text)
    elif (choice == 'fr-en'):
        return frensh_to_english(user_text)
    else:
        return {'warning':'out of choices en-fr , fr-en'}
    

# @app.post('/register')
# def register():
#     pass

# @app.post('/login')
# def login():
#     pass