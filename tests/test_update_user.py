from api.user_api import UserAPI
from data.user_payload import create_user_payload


def test_update_user():

    payload = create_user_payload()

    create = UserAPI.create_user(payload)
    user_id = create.json()["id"]

    update_data = {"name": "Updated User"}

    response = UserAPI.update_user(user_id, update_data)

    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"

def test_update_user():
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

    update_data = {"name": "Updated User"}
    response = UserAPI.update_user(user_id, update_data)

    print("UPDATE STATUS:", response.status_code)
    print("UPDATE BODY:", response.text)
    
    assert response.status_code == 200, f"Update failed: {response.text}"

    try:
        data = response.json()
    except Exception as e:
        raise AssertionError(f"Invalid JSON (update): {response.text}") from e

    assert data.get("name") == "Updated User", "Update name failed"
