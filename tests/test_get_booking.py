import requests

def test_get_booking_success(url):
    booking_id = 1  # Убедитесь, что этот ID существует
    response = requests.get(f"{url}/booking/{booking_id}")
    assert response.status_code == 200

def test_get_booking_failure(url):
    booking_id = 99999  # Несуществующий ID
    response = requests.get(f"{url}/booking/{booking_id}")
    assert response.status_code == 404
