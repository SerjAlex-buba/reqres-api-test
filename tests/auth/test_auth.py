
import requests
import pytest

def test_login_success(base_url):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f"{base_url}/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()


@pytest.mark.parametrize("payload", [
    {"email": "eve.holt@reqres.in"},              # нет пароля
    {"password": "cityslicka"},                   # нет email
    {},                                           # пустой json
])
def test_login_failure(base_url, payload):
    response = requests.post(f"{base_url}/login", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()
