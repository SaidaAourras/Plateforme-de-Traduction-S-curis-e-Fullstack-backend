from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth')

@auth_router.post('/register')
def register():
     pass

# @app.post('/login')
# def login():
#     pass