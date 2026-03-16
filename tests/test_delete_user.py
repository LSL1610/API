from api.user_api import UserAPI
from data.user_payload import create_user_payload


def test_delete_user():

    payload = create_user_payload()

    create = UserAPI.create_user(payload)
    user_id = create.json()["id"]

    delete = UserAPI.delete_user(user_id)

    assert delete.status_code == 204
