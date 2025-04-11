import requests
import pytest


def test_delete_user(base_url):
    user_id = 2
    response = requests.delete(f"{base_url}/users/{user_id}")

    assert response.status_code == 204
    assert response.text == ""  # Тело ответа должно быть пустым
