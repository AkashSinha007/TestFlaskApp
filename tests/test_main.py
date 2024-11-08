# tests/test_main.py
from app.main import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.json == {"message": "Hello, World!"}
