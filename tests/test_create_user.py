from api.user_api import UserAPI
from data.user_payload import create_user_payload


def test_create_user():

    payload = create_user_payload()

    response = UserAPI.create_user(payload)

    assert response.status_code == 201
    assert response.json()["email"] == payload["email"]
