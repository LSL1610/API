import pytest 
from api.user_api import UserAPI
from data.user_payload import create_user_payload
from faker import Faker

fake = Faker()

@pytest.mark.parametrize("payload", [
    {"name": fake.name(), "email": fake.email(), "gender": "male", "status": "active"},
    {"name": fake.name(), "email": fake.email(), "gender": "female", "status": "active"},
    {"name": fake.name(), "email": fake.email(), "gender": "male", "status": "active"},
    {"name": fake.name(), "email": fake.email(), "gender": "female", "status": "active"},
])
def test_create_user(payload):
    response = UserAPI.create_user(payload)
    
    print("STATUS:", response.status_code)
    print("BODY:", response.text)

    assert response.status_code == 201, f"Create failed: {response.text}"
    try:
        data = response.json()
    except Exception as e:
        raise AssertionError(f"Response is not valid JSON: {response.text}") from e

    assert data.get("email") == payload.get("email"), "Email mismatch"

