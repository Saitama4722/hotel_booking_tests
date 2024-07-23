import requests

def test_auth_success(url):
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{url}/auth", json=data)
    assert response.status_code == 200
    assert "token" in response.json()

def test_auth_failure(url):
    data = {
        "username": "wrong_user",
        "password": "wrong_pass"
    }
    response = requests.post(f"{url}/auth", json=data)
    assert response.status_code == 401
