import requests
import pytest

def test_get_users_page_2(base_url):
    response = requests.get(f"{base_url}/users", params={"page": 2})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data["page"] == 2
    assert "data" in json_data
    assert isinstance(json_data["data"], list)
    assert len(json_data["data"]) > 0

    # Проверим структуру первого пользователя
    user = json_data["data"][0]
    for key in ["id", "email", "first_name", "last_name", "avatar"]:
        assert key in user

def test_get_users_invalid_page(base_url):
    response = requests.get(f"{base_url}/users", params={"page": 999})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data["data"] == []  # Возвращается пустой список
