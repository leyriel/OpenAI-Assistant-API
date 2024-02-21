import requests


def register_user(username, email, password):
    url = "http://localhost:1337/api/auth/local/register"
    data = {
        "username": username,
        "email": email,
        "password": password
    }
    response = requests.post(url, json=data)

    return response.json()
