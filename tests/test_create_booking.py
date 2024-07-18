import requests

def test_create_booking_success():
    url = "https://restful-booker.herokuapp.com/booking"
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-14",
            "checkout": "2024-07-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert "bookingid" in response.json()

def test_create_booking_failure():
    url = "https://restful-booker.herokuapp.com/booking"
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": "invalid_price",  # Некорректное значение
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-14",
            "checkout": "2024-07-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400  # Ожидаемый код состояния при неудаче

def test_create_booking_failure_missing_field():
    url = "https://restful-booker.herokuapp.com/booking"
    data = {
        "lastname": "Brown",  # Отсутствует firstname
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-14",
            "checkout": "2024-07-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 400  # Ожидаемый код состояния при неудаче
