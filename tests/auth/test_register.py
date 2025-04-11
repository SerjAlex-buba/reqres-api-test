import requests
import pytest

@pytest.mark.parametrize("email, password, expected_status, expected_key", [
    ("eve.holt@reqres.in", "pistol", 200, "token"),      # ✅ Позитивный кейс
    ("eve.holt@reqres.in", "", 400, "error"),            # 🚫 Нет пароля
    ("", "pistol", 400, "error"),                        # 🚫 Нет email
    ("wrong@mail.com", "12345", 400, "error"),           # 🚫 Неверные данные
])
def test_register(base_url,email, password, expected_status, expected_key):
    response = requests.post(f"{base_url}/register", json={
        "email": email,
        "password": password
    })

    print("RESPONSE:", response.json())  # для отладки
    assert response.status_code == expected_status
    assert expected_key in response.json()

