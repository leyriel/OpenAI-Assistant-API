import requests


def get_user_info(token, serialized_response=True):
    url = "http://localhost:1337/api/users/me"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)

    if not serialized_response:
        return response

    return response.json()
