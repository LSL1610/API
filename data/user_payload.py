from faker import Faker

fake = Faker()


def create_user_payload():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "gender": "male",
        "status": "active"
    }
