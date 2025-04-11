import pytest

BASE_URL = "https://reqres.in/api"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL