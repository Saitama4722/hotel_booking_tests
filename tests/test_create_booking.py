import requests
import pytest

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
        "totalprice": "eleven",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-14",
            "checkout": "2024-07-15"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url, json=data)
    assert response.status_code == 500
