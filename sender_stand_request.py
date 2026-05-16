import requests
import configuration
import data
from data import kit_body


def post_new_user(user_body):
    return requests.post(
        configuration.BASE_URL + configuration.CREATE_USER_PATH,
        json=user_body,
        headers=data.headers
    )

def post_new_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    print(kit_body)
    return requests.post(
        configuration.BASE_URL + configuration.CREATE_KIT_PATH,
        json=kit_body,
        headers=headers
    )
