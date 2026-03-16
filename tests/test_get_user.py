from api.user_api import UserAPI
from data.user_payload import create_user_payload
from loguru import logger

def test_get_user():

    payload = create_user_payload()

    create = UserAPI.create_user(payload)
    user_id = create.json()["id"]

    response = UserAPI.get_user(user_id)
    logger.warning(response.text)

    assert response.status_code == 200
    assert response.json()["id"] == user_id
