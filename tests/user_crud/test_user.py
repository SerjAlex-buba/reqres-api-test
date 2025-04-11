import requests
import pytest


def test_get_single_user_success(base_url):
    user_id = 2
    response = requests.get(f"{base_url}/users/{user_id}")
    json_data = response.json()

    assert response.status_code == 200
    assert "data" in json_data

    user = json_data["data"]
    assert user["id"] == user_id
    assert "email" in user
    assert "first_name" in user
    assert "last_name" in user
    assert "avatar" in user
def test_get_single_user_not_found(base_url):
    user_id = 23
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 404
    assert response.text == "{}"  # ответ — пустой JSON

