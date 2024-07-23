import requests
import pytest

@pytest.mark.qase(1)  # Используйте правильный ID теста
def test_auth_success(url):
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{url}/auth", json=data)
    assert response.status_code == 200
    assert "token" in response.json()

@pytest.mark.qase("HBT")
def test_auth_failure(url):
    auth_url = f"{url}/auth"
    data = {
        "username": "wrong_user",
        "password": "wrong_password"
    }
    response = requests.post(auth_url, json=data)
    assert response.status_code == 200
    assert "reason" in response.json()
