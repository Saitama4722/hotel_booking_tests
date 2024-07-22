import requests

def test_create_booking_success(url):
    response = requests.post(f"{url}/booking", json={})
    assert response.status_code == 200

def test_create_booking_failure(url):
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": "not-boolean",
        "bookingdates": {
            "checkin": "2024-07-14",
            "checkout": "2024-07-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{url}/booking", json=data)
    assert response.status_code == 400

def test_create_booking_failure_missing_field(url):
    data = {
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-14",
            "checkout": "2024-07-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{url}/booking", json=data)
    assert response.status_code == 400
