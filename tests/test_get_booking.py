import requests
import pytest

@pytest.mark.qase(5)  # Используйте правильный ID теста
def test_get_booking_success(url):
    booking_id = 1
    response = requests.get(f"{url}/booking/{booking_id}")
    assert response.status_code == 200

@pytest.mark.qase(6)  # Используйте правильный ID теста
def test_get_booking_failure(url):
    booking_id = 9999999
    response = requests.get(f"{url}/booking/{booking_id}")
    assert response.status_code == 404
