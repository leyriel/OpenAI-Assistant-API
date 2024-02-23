import requests


def get_user_info(token):
    url = "http://localhost:1337/api/users/me"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()
