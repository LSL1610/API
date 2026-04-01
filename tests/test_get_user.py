from api.user_api import UserAPI
from data.user_payload import create_user_payload
from loguru import logger

def test_get_user():
    payload = create_user_payload()
    create = UserAPI.create_user(payload)

    print("CREATE STATUS:", create.status_code)
    print("CREATE BODY:", create.text)

    assert create.status_code == 201, f"Create failed: {create.text}"

    try:
        create_data = create.json()
    except Exception as e:
        raise AssertionError(f"Invalid JSON (create): {create.text}") from e

    user_id = create_data.get("id")
    assert user_id is not None, "User ID not found"

    response = UserAPI.get_user(user_id)

    print("GET STATUS:", response.status_code)
    print("GET BODY:", response.text)

    assert response.status_code == 200, f"Get user failed: {response.text}"

    try:
        data = response.json()
    except Exception as e:
        raise AssertionError(f"Invalid JSON (get): {response.text}") from e

    assert data.get("id") == user_id, "User ID mismatch"
