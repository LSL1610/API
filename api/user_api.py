import requests
from utils.config import BASE_URL, HEADERS


class UserAPI:

    @staticmethod
    def create_user(payload):
        return requests.post(
            f"{BASE_URL}/users",
            headers=HEADERS,
            json=payload
        )

    @staticmethod
    def get_user(user_id):
        return requests.get(
            f"{BASE_URL}/users/{user_id}",
            headers=HEADERS
        )

    @staticmethod
    def update_user(user_id, payload):
        return requests.put(
            f"{BASE_URL}/users/{user_id}",
            headers=HEADERS,
            json=payload
        )

    @staticmethod
    def delete_user(user_id):
        return requests.delete(
            f"{BASE_URL}/users/{user_id}",
            headers=HEADERS
        )
