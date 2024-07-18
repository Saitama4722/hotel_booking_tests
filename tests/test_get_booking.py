import requests
import pytest

def test_get_booking_success():
    booking_id = 1
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert "firstname" in response.json()

def test_get_booking_failure():
    booking_id = 999999
    url = f"https://restful-booker.herokuapp.com/booking/{booking_id}"
    response = requests.get(url)
    assert response.status_code == 404