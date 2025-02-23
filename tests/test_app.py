import requests

BASE_URL = "http://localhost:5000"

def test_add():
    response = requests.get(f"{BASE_URL}/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json()['result'] == 8

def test_subtract():
    response = requests.get(f"{BASE_URL}/subtract?a=10&b=4")
    assert response.status_code == 200
    assert response.json()['result'] == 6

def test_multiply():
    response = requests.get(f"{BASE_URL}/multiply?a=3&b=3")
    assert response.status_code == 200
    assert response.json()['result'] == 9

def test_divide():
    response = requests.get(f"{BASE_URL}/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json()['result'] == 5

