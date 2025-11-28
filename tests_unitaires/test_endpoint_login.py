from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_endpoint_login():
    response = client.post('http://127.0.0.1:8000/api/v1/auth/login',data={
        "grant_type": "password",
        "username": 'saida@gmail.com',
        "password": '12345'
    })
    
    assert response.status_code == 200