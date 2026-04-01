from api.user_api import UserAPI
from data.user_payload import create_user_payload


def test_delete_user():
    payload = create_user_payload()

    create = UserAPI.create_user(payload)

    assert create.status_code == 201, f"Create failed: {create.text}"

    try:
        create_data = create.json()
    except Exception as e:
        raise AssertionError(f"Invalid JSON response: {create.text}") from e

    user_id = create_data.get("id")
    assert user_id is not None, "User ID not found in response"

    delete = UserAPI.delete_user(user_id)

    print("DELETE STATUS:", delete.status_code)
    print("DELETE BODY:", delete.text)

    assert delete.status_code == 204, f"Delete failed: {delete.text}"
