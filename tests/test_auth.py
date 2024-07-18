import requests

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
        "username": "invalid_user",
        "password": "invalid_pass"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200  # Ожидаемый код состояния при неудаче
    assert "token" not in response.json()
