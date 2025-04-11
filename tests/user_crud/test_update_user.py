import requests
import pytest


def test_update_user_put(base_url):
    user_id = 2
    payload = {
        "name": "neo",
        "job": "the one"
    }

    response = requests.put(f"{base_url}/users/{user_id}", json=payload)
    json_data = response.json()

    assert response.status_code == 200
    assert json_data["name"] == payload["name"]
    assert json_data["job"] == payload["job"]
    assert "updatedAt" in json_data


def test_update_user_patch(base_url):
    user_id = 2
    payload = {
        "job": "chosen one"
    }

    response = requests.patch(f"{base_url}/users/{user_id}", json=payload)
    json_data = response.json()

    assert response.status_code == 200
    assert json_data["job"] == payload["job"]
    assert "updatedAt" in json_data

