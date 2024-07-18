import requests
import pytest

def test_auth_success():
    url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert "token" in response.json()

def test_auth_failure():
    url = "https://restful-booker.herokuapp.com/auth"
    data = {
        "username": "admin",
        "password": "wrongpassword"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert "reason" in response.json()
    assert response.json()["reason"] == "Bad credentials"
