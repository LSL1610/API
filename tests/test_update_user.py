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
