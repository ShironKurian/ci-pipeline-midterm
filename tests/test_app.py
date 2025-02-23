import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add?a=5&b=3')
    assert response.status_code == 200
    assert response.get_json() == {"result": 8}

def test_subtract(client):
    response = client.get('/subtract?a=10&b=3')
    assert response.status_code == 200
    assert response.get_json() == {"result": 7}

def test_multiply(client):
    response = client.get('/multiply?a=4&b=6')
    assert response.status_code == 200
    assert response.get_json() == {"result": 24}

def test_divide(client):
    response = client.get('/divide?a=8&b=2')
    assert response.status_code == 200
    assert response.get_json() == {"result": 4}