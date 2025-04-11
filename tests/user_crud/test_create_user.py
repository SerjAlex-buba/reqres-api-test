import requests
import pytest


def test_create_user_success(base_url):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(f"{base_url}/users", json=payload)
    json_data = response.json()

    assert response.status_code == 201
    assert json_data["name"] == payload["name"]
    assert json_data["job"] == payload["job"]
    assert "id" in json_data
    assert "createdAt" in json_data

def test_create_user_empty_payload(base_url):
    response = requests.post(f"{base_url}/users", json={})
    json_data = response.json()

    assert response.status_code == 201
    assert "id" in json_data
    assert "createdAt" in json_data
    # Но нет имени и работы — проверим это
    assert json_data.get("name") is None
    assert json_data.get("job") is None
