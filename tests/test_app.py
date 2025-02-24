import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_add(client):
    response = client.get('/add?a=5&b=3')
    assert response.status_code == 200
    assert response.json['result'] == 8

def test_subtract(client):
    response = client.get('/subtract?a=10&b=4')
    assert response.status_code == 200
    assert response.json['result'] == 6

def test_multiply(client):
    response = client.get('/multiply?a=3&b=7')
    assert response.status_code == 200
    assert response.json['result'] == 21

def test_divide(client):
    response = client.get('/divide?a=20&b=5')
    assert response.status_code == 200
    assert response.json['result'] == 4

def test_divide_by_zero(client):
    response = client.get('/divide?a=20&b=0')
    assert response.status_code == 400
    assert response.json['error'] == "Division by zero is not allowed"